## Module containing checks performed on a SampleSheet file for Illumina sequencers
from  iSkyLIMS_wetlab.models import *
import os
import pdb

from django.conf import settings
from .sample_convertion import get_projects_in_run

def timestamp_print(message):
    starting_time= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(starting_time+' '+message)

def check_run_name_free_to_use(run_name):
    ## Function checks whether run_name is already used in the database.
    ## Error page is shown if run_name is already  defined
    ##

    timestamp_print('Starting the process for check_run_name_free_to_use()')
    run_name_free_result='KO in check_run_name_free_to_use()'
    timestamp_print('(experiment)Run name: '+run_name)
    if (RunProcess.objects.filter(runName = run_name)).exists():
        if RunProcess.objects.filter(runName = run_name, runState__exact ='Pre-Recorded'):
            ## Delete the sample sheet file and the row in database
            delete_run = RunProcess.objects.filter(runName = run_name, runState__exact ='Pre-Recorded')
            sample_sheet_file = str(delete_run[0].sampleSheet)
            full_path_sample_sheet_file = os.path.join(settings.MEDIA_ROOT, sample_sheet_file)
            os.remove(full_path_sample_sheet_file)
            delete_run[0].delete()
            run_name_free_result='Free'
        else:#runState != 'Pre-Recorded'
            run_name_free_result=['Run Name is already used. ',
                                  'Run Name must be unique in database.', ' ',
                                  'ADVICE:',
                                  'Change the value in the Sample Sheet  file ']
    else: # run_name is new
        run_name_free_result='Free'

    timestamp_print('Leaving check_run_name_free_to_use(). Returned value= '+str(run_name_free_result))
    return run_name_free_result



def check_run_projects_in_samplesheet(samplesheet):
    ## Check that there are projects with researchers  declared within the run
    timestamp_print('Starting the process for check_run_projects_in_samplesheet()')
    project_list=get_projects_in_run(samplesheet)
    timestamp_print('project_list= '+str(project_list))
    message_output='KO in check_run_projects_in_samplesheet'

    if len (project_list) == 0 :
        message_output=[
            'Sample Sheet does not contain "Sample project" and/or "Description" fields',
            '', 'ADVICE:',
            'Check that csv file generated by Illumina Experient Manager'
            ' (IEM) includes these columns']
    else:
        for key,val in project_list.items():
            if ''==val:##no researcher associated with project
                message_output=['Sample Sheet does not contain "Description" fields',
                    '', 'ADVICE:',
                    'Check that csv file generated by Illumina Experient Manager'
                    ' (IEM) includes this column']
                break;

            elif ''==key:
                message_output=['Sample Sheet does not contain "Sample Project" fields',
                    '', 'ADVICE:',
                    'Check that csv file generated by Illumina Experient Manager'
                    ' (IEM) includes this column']
                break;

            else:
                message_output='OK_projects_samplesheet'

    timestamp_print('Leaving check_run_projects_in_samplesheet(). Returned value= '+str(message_output))
    return message_output



def check_run_users_definition(samplesheet):
    ## CHECK if the users are already defined in database.
    timestamp_print('Starting the process for check_run_users_definition()')
    message_output='KO in check_run_users_definition'
    user_not_defined=[]
    project_list=get_projects_in_run(samplesheet)
    timestamp_print('project_list= '+str(project_list))

    for key, val  in project_list.items():
        if ( not User.objects.filter(username__icontains = val).exists()):
            user_not_defined.append(val)
    if (len(user_not_defined)>0):
        if (len(user_not_defined)>1):
            head_text='The following users are not defined in database:'
        else:
            head_text='The following user is not defined in database:'
        ## convert the list into string to display the user names on error page
        display_user= ' ,  '.join(user_not_defined)
        message_output=[head_text,'', display_user,'',
            'Researcher names must be installed in database before uploading the Sample sheet']
    else:
        message_output='OK_users'

    timestamp_print('Leaving check_run_users_definition(). Returned value= '+str(message_output))
    return message_output



def check_run_projects_definition(project_list):
    ## Check that the projects are NOT already defined in the database
    timestamp_print('Starting the process for check_run_projects_definition()')
    timestamp_print('project_list= '+str(project_list))
    message_output='KO in check_run_projects_definition'
    project_already_defined=[]
    for key, val  in project_list.items():
        # check if project was already saved in database in Not Started State.
        # if found delete the projects, because the previous attempt to complete the run was unsuccessful
        if ( Projects.objects.filter(projectName__icontains = key).exists()):
            if ( Projects.objects.filter(projectName__icontains = key, procState__exact = 'Not Started').exists()):
                delete_project = Projects.objects.filter(projectName__icontains = key , procState__exact = 'Not Started')
                delete_project[0].delete()
            else:
                project_already_defined.append(key)
    if (len(project_already_defined)>0):
        if (len(project_already_defined)>1):
            head_text='The following projects are already defined in database:'
        else:
            head_text='The following project is already defined in database:'
        ## convert the list into string to display the user names on error page
        display_project= '  '.join(project_already_defined)
        message_output= [ head_text,'', display_project,'',
                        'Project names must be unique', '', 'ADVICE:',
                        'Edit the Sample Sheet file to correct this error']
    else:
        message_output="OK_projects_db"

    timestamp_print('Leaving check_run_projects_definition(). Returned value= '+str(message_output))
    return message_output
