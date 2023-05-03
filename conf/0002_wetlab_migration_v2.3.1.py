# Generated by Django 3.2 on 2023-04-29 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
        ("wetlab", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AdditionaKitsLibraryPreparation",
            new_name="AdditionaKitsLibPrepare",
        ),
        migrations.RenameModel(
            old_name="StatesForPool",
            new_name="PoolStates",
        ),
        migrations.RenameModel(
            old_name="StatesForLibraryPreparation",
            new_name="LibPrepareStates",
        ),
        migrations.RenameModel(
            old_name="libPreparationUserSampleSheet",
            new_name="LibUserSampleSheet",
        ),
        migrations.AlterModelOptions(
            name="librarypool",
            options={"ordering": ("pool_name",)},
        ),
        migrations.RenameField(
            model_name="additionakitslibprepare",
            old_name="commercialKit_id",
            new_name="commercial_kit_id",
        ),
        migrations.RenameField(
            model_name="additionakitslibprepare",
            old_name="kitName",
            new_name="kit_name",
        ),
        migrations.RenameField(
            model_name="additionakitslibprepare",
            old_name="kitOrder",
            new_name="kit_order",
        ),
        migrations.RenameField(
            model_name="additionakitslibprepare",
            old_name="kitUsed",
            new_name="kit_used",
        ),
        migrations.RenameField(
            model_name="additionakitslibprepare",
            old_name="registerUser",
            new_name="register_user",
        ),
        migrations.RenameField(
            model_name="additionaluserlotkit",
            old_name="additionalLotKits",
            new_name="additional_lot_kits",
        ),
        migrations.RenameField(
            model_name="additionaluserlotkit",
            old_name="userLotKit_id",
            new_name="user_lot_kit_id",
        ),
        migrations.RenameField(
            model_name="collectionindexkit",
            old_name="adapter1",
            new_name="adapter_1",
        ),
        migrations.RenameField(
            model_name="collectionindexkit",
            old_name="adapter2",
            new_name="adapter_2",
        ),
        migrations.RenameField(
            model_name="collectionindexkit",
            old_name="collectionIndexName",
            new_name="collection_index_name",
        ),
        migrations.RenameField(
            model_name="collectionindexkit",
            old_name="generatedat",
            new_name="generated_at",
        ),
        migrations.RenameField(
            model_name="collectionindexkit",
            old_name="plateExtension",
            new_name="plate_extension",
        ),
        migrations.RenameField(
            model_name="collectionindexvalues",
            old_name="collectionIndexKit_id",
            new_name="collection_index_kit_id",
        ),
        migrations.RenameField(
            model_name="collectionindexvalues",
            old_name="defaultWell",
            new_name="default_well",
        ),
        migrations.RenameField(
            model_name="configsetting",
            old_name="configurationName",
            new_name="configuration_name",
        ),
        migrations.RenameField(
            model_name="configsetting",
            old_name="configurationValue",
            new_name="configuration_value",
        ),
        migrations.RenameField(
            model_name="graphicsstats",
            old_name="cluserCountGraph",
            new_name="cluster_count_graph",
        ),
        migrations.RenameField(
            model_name="graphicsstats",
            old_name="flowCellGraph",
            new_name="flowcell_graph",
        ),
        migrations.RenameField(
            model_name="graphicsstats",
            old_name="folderRunGraphic",
            new_name="folder_run_graphic",
        ),
        migrations.RenameField(
            model_name="graphicsstats",
            old_name="heatMapGraph",
            new_name="heatmap_graph",
        ),
        migrations.RenameField(
            model_name="graphicsstats",
            old_name="histogramGraph",
            new_name="histogram_graph",
        ),
        migrations.RenameField(
            model_name="graphicsstats",
            old_name="intensityByCycleGraph",
            new_name="intensity_by_cycle_graph",
        ),
        migrations.RenameField(
            model_name="graphicsstats",
            old_name="sampleQcGraph",
            new_name="sample_qc_graph",
        ),
        migrations.RenameField(
            model_name="libparametervalue",
            old_name="parameterValue",
            new_name="parameter_value",
        ),
        migrations.RenameField(
            model_name="libpreparestates",
            old_name="libPrepState",
            new_name="lib_prep_state",
        ),
        migrations.RenameField(
            model_name="librarykit",
            old_name="generatedat",
            new_name="generated_at",
        ),
        migrations.RenameField(
            model_name="librarykit",
            old_name="libraryName",
            new_name="library_name",
        ),
        migrations.RenameField(
            model_name="librarypool",
            old_name="pairedEnd",
            new_name="paired_end",
        ),
        migrations.RenameField(
            model_name="librarypool",
            old_name="poolCodeID",
            new_name="pool_code_id",
        ),
        migrations.RenameField(
            model_name="librarypool",
            old_name="poolName",
            new_name="pool_name",
        ),
        migrations.RenameField(
            model_name="librarypool",
            old_name="poolState",
            new_name="pool_state",
        ),
        migrations.RenameField(
            model_name="librarypool",
            old_name="registerUser",
            new_name="register_user",
        ),
        migrations.RenameField(
            model_name="librarypool",
            old_name="runProcess_id",
            new_name="run_process_id",
        ),
        migrations.RenameField(
            model_name="librarypool",
            old_name="numberOfSamples",
            new_name="sample_number",
        ),
        migrations.RenameField(
            model_name="libusersamplesheet",
            old_name="adapter1",
            new_name="adapter_1",
        ),
        migrations.RenameField(
            model_name="libusersamplesheet",
            old_name="adapter2",
            new_name="adapter_2",
        ),
        migrations.RenameField(
            model_name="libusersamplesheet",
            old_name="collectionIndexKit_id",
            new_name="collection_index_kit_id",
        ),
        migrations.RenameField(
            model_name="libusersamplesheet",
            old_name="confirmedUsed",
            new_name="confirmed_used",
        ),
        migrations.RenameField(
            model_name="libusersamplesheet",
            old_name="generatedat",
            new_name="generated_at",
        ),
        migrations.RenameField(
            model_name="libusersamplesheet",
            old_name="iemVersion",
            new_name="iem_version",
        ),
        migrations.RenameField(
            model_name="libusersamplesheet",
            old_name="registerUser",
            new_name="register_user",
        ),
        migrations.RenameField(
            model_name="libusersamplesheet",
            old_name="sampleSheet",
            new_name="sample_sheet",
        ),
        migrations.RenameField(
            model_name="libusersamplesheet",
            old_name="sequencingConfiguration",
            new_name="sequencing_configuration",
        ),
        migrations.RenameField(
            model_name="poolstates",
            old_name="poolState",
            new_name="pool_state",
        ),
        migrations.RenameField(
            model_name="projects",
            old_name="baseSpaceFile",
            new_name="base_space_file",
        ),
        migrations.RenameField(
            model_name="projects",
            old_name="BaseSpaceLibrary",
            new_name="base_space_library",
        ),
        migrations.RenameField(
            model_name="projects",
            old_name="generatedat",
            new_name="generated_at",
        ),
        migrations.RenameField(
            model_name="projects",
            old_name="libraryKit",
            new_name="library_kit",
        ),
        migrations.RenameField(
            model_name="projects",
            old_name="LibraryKit_id",
            new_name="library_kit_id",
        ),
        migrations.RenameField(
            model_name="projects",
            old_name="projectName",
            new_name="project_name",
        ),
        migrations.RenameField(
            model_name="projects",
            old_name="runProcess",
            new_name="run_process",
        ),
        migrations.RenameField(
            model_name="rawdemuxstats",
            old_name="defaultAll",
            new_name="default_all",
        ),
        migrations.RenameField(
            model_name="rawdemuxstats",
            old_name="PF_QualityScore",
            new_name="pf_quality_score",
        ),
        migrations.RenameField(
            model_name="rawdemuxstats",
            old_name="PF_Yield",
            new_name="pf_yield",
        ),
        migrations.RenameField(
            model_name="rawdemuxstats",
            old_name="PF_YieldQ30",
            new_name="pf_yield_q30",
        ),
        migrations.RenameField(
            model_name="rawdemuxstats",
            old_name="rawQuality",
            new_name="raw_quality",
        ),
        migrations.RenameField(
            model_name="rawdemuxstats",
            old_name="rawYield",
            new_name="raw_yield",
        ),
        migrations.RenameField(
            model_name="rawdemuxstats",
            old_name="rawYieldQ30",
            new_name="raw_yield_q30",
        ),
        migrations.RenameField(
            model_name="runconfigurationtest",
            old_name="runTestFolder",
            new_name="run_test_folder",
        ),
        migrations.RenameField(
            model_name="runconfigurationtest",
            old_name="runTestName",
            new_name="run_test_name",
        ),
        migrations.RenameField(
            model_name="runerrors",
            old_name="errorCode",
            new_name="error_code",
        ),
        migrations.RenameField(
            model_name="runerrors",
            old_name="errorText",
            new_name="error_text",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="AnalysisWorkflowType",
            new_name="analysis_workflow_type",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="ApplicationVersion",
            new_name="application_version",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="Chemistry",
            new_name="chemistry",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="ExperimentName",
            new_name="experiment_name",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="Flowcell",
            new_name="flowcell",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="FlowcellLayout",
            new_name="flowcell_layout",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="ImageChannel",
            new_name="image_channel",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="ImageDimensions",
            new_name="image_dimensions",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="LibraryID",
            new_name="library_id",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="NumTilesPerSwath",
            new_name="num_tiles_per_swath",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="PlannedIndex1ReadCycles",
            new_name="planned_index1_read_cycles",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="PlannedIndex2ReadCycles",
            new_name="planned_index2_read_cycles",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="PlannedRead1Cycles",
            new_name="planned_read1_cycles",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="PlannedRead2Cycles",
            new_name="planned_read2_cycles",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="RTAVersion",
            new_name="rta_version",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="RunID",
            new_name="run_id",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="RunManagementType",
            new_name="run_management_type",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="runName_id",
            new_name="run_name_id",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="RunStartDate",
            new_name="run_start_date",
        ),
        migrations.RenameField(
            model_name="runningparameters",
            old_name="SystemSuiteVersion",
            new_name="system_suite_version",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="centerRequestedBy",
            new_name="center_requested_by",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="generatedat",
            new_name="generated_at",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="runError",
            new_name="run_error",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="runName",
            new_name="run_name",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="sampleSheet",
            new_name="sample_sheet",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="stateBeforeError",
            new_name="state_before_error",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="useSpaceFastaMb",
            new_name="use_space_fasta_mb",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="useSpaceImgMb",
            new_name="use_space_img_mb",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="useSpaceOtherMb",
            new_name="use_space_other_mb",
        ),
        migrations.RenameField(
            model_name="runprocess",
            old_name="usedSequencer",
            new_name="used_sequencer",
        ),
        migrations.RenameField(
            model_name="runstates",
            old_name="runStateName",
            new_name="run_state_name",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_APPLICATION_FOLDER_NAME",
            new_name="domain",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_DOMAIN",
            new_name="host_name",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_IP_SERVER",
            new_name="ip_server",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="IS_DIRECT_TCP",
            new_name="is_direct_tcp",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_NTLM_USED",
            new_name="ntlm_used",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_PORT_SERVER",
            new_name="port_server",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_HOST_NAME",
            new_name="remote_server_name",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_REMOTE_SERVER_NAME",
            new_name="samba_folder_name",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_SHARED_FOLDER_NAME",
            new_name="shared_folder_name",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_USER_ID",
            new_name="user_id",
        ),
        migrations.RenameField(
            model_name="sambaconnectiondata",
            old_name="SAMBA_USER_PASSWORD",
            new_name="user_password",
        ),
        migrations.RenameField(
            model_name="samplesinproject",
            old_name="barcodeName",
            new_name="barcode_name",
        ),
        migrations.RenameField(
            model_name="samplesinproject",
            old_name="meanQuality",
            new_name="mean_quality",
        ),
        migrations.RenameField(
            model_name="samplesinproject",
            old_name="percentInProject",
            new_name="percent_in_project",
        ),
        migrations.RenameField(
            model_name="samplesinproject",
            old_name="pfClusters",
            new_name="pf_clusters",
        ),
        migrations.RenameField(
            model_name="samplesinproject",
            old_name="qualityQ30",
            new_name="quality_q30",
        ),
        migrations.RenameField(
            model_name="samplesinproject",
            old_name="runProcess_id",
            new_name="run_process_id",
        ),
        migrations.RenameField(
            model_name="samplesinproject",
            old_name="sampleInCore",
            new_name="sample_in_core",
        ),
        migrations.RenameField(
            model_name="samplesinproject",
            old_name="sampleName",
            new_name="sample_name",
        ),
        migrations.RenameField(
            model_name="samplesinproject",
            old_name="yieldMb",
            new_name="yield_mb",
        ),
        migrations.RenameField(
            model_name="statsflsummary",
            old_name="defaultAll",
            new_name="default_all",
        ),
        migrations.RenameField(
            model_name="statsflsummary",
            old_name="flowPfCluster",
            new_name="flow_pf_cluster",
        ),
        migrations.RenameField(
            model_name="statsflsummary",
            old_name="flowRawCluster",
            new_name="flow_raw_cluster",
        ),
        migrations.RenameField(
            model_name="statsflsummary",
            old_name="flowYieldMb",
            new_name="flow_yield_mb",
        ),
        migrations.RenameField(
            model_name="statsflsummary",
            old_name="sampleNumber",
            new_name="sample_number",
        ),
        migrations.RenameField(
            model_name="statslanesummary",
            old_name="biggerQ30",
            new_name="bigger_q30",
        ),
        migrations.RenameField(
            model_name="statslanesummary",
            old_name="defaultAll",
            new_name="default_all",
        ),
        migrations.RenameField(
            model_name="statslanesummary",
            old_name="meanQuality",
            new_name="mean_quality",
        ),
        migrations.RenameField(
            model_name="statslanesummary",
            old_name="oneMismatch",
            new_name="one_mismatch",
        ),
        migrations.RenameField(
            model_name="statslanesummary",
            old_name="percentLane",
            new_name="percent_lane",
        ),
        migrations.RenameField(
            model_name="statslanesummary",
            old_name="perfectBarcode",
            new_name="perfect_barcode",
        ),
        migrations.RenameField(
            model_name="statslanesummary",
            old_name="pfCluster",
            new_name="pf_cluster",
        ),
        migrations.RenameField(
            model_name="statslanesummary",
            old_name="yieldMb",
            new_name="yield_mb",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="cluster_PF",
            new_name="cluster_pf",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="cyclesErrRated",
            new_name="cycles_err_rated",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="errorRate",
            new_name="error_rate",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="errorRate100",
            new_name="error_rate_100",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="errorRate35",
            new_name="error_rate_35",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="errorRate50",
            new_name="error_rate_50",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="errorRate75",
            new_name="error_rate_75",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="generatedat",
            new_name="generated_at",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="intensityCycle",
            new_name="intensity_cycle",
        ),
        migrations.RenameField(
            model_name="statsrunread",
            old_name="reads_PF",
            new_name="reads_pf",
        ),
        migrations.RenameField(
            model_name="statsrunsummary",
            old_name="biggerQ30",
            new_name="bigger_q30",
        ),
        migrations.RenameField(
            model_name="statsrunsummary",
            old_name="errorRate",
            new_name="error_rate",
        ),
        migrations.RenameField(
            model_name="statsrunsummary",
            old_name="generatedat",
            new_name="generated_at",
        ),
        migrations.RenameField(
            model_name="statsrunsummary",
            old_name="intensityCycle",
            new_name="intensity_cycle",
        ),
        migrations.RenameField(
            model_name="statsrunsummary",
            old_name="projectedTotalYield",
            new_name="projected_total_yield",
        ),
        migrations.RenameField(
            model_name="statsrunsummary",
            old_name="yieldTotal",
            new_name="yield_total",
        ),
        migrations.RenameField(
            model_name="collectionindexkit",
            old_name="collectionIndexFile",
            new_name="collection_index_file",
        ),
        migrations.AlterField(
            model_name="collectionindexkit",
            name="collection_index_file",
            field=models.FileField(
                default=None, max_length=500, upload_to="wetlab/collection_index_kits/"
            ),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name="additionakitslibprepare",
            table="wetlab_lib_additional_kits_lib_prepare",
        ),
        migrations.AlterModelTable(
            name="additionaluserlotkit",
            table="wetlab_lib_additional_user_lot_kit",
        ),
        migrations.AlterModelTable(
            name="collectionindexkit",
            table="wetlab_collection_index_kit",
        ),
        migrations.AlterModelTable(
            name="collectionindexvalues",
            table="wetlab_collection_index_values",
        ),
        migrations.AlterModelTable(
            name="configsetting",
            table="wetlab_config_setting",
        ),
        migrations.AlterModelTable(
            name="graphicsstats",
            table="wetlab_graphics_stats",
        ),
        migrations.AlterModelTable(
            name="libparametervalue",
            table="wetlab_lib_parameter_value",
        ),
        migrations.AlterModelTable(
            name="libpreparestates",
            table="wetlab_lib_prepare_states",
        ),
        migrations.AlterModelTable(
            name="librarykit",
            table="wetlab_library_kit",
        ),
        migrations.AlterModelTable(
            name="librarypool",
            table="wetlab_library_pool",
        ),
        migrations.AlterModelTable(
            name="libusersamplesheet",
            table="wetlab_lib_user_samplesheet",
        ),
        migrations.AlterModelTable(
            name="poolstates",
            table="wetlab_pool_states",
        ),
        migrations.AlterModelTable(
            name="projects",
            table="wetlab_projects",
        ),
        migrations.AlterModelTable(
            name="rawdemuxstats",
            table="wetlab_raw_demux_stats",
        ),
        migrations.AlterModelTable(
            name="rawtopunknowbarcodes",
            table="wetlab_raw_top_unknown_barcodes",
        ),
        migrations.AlterModelTable(
            name="runconfigurationtest",
            table="wetlab_lib_run_configuration_test",
        ),
        migrations.AlterModelTable(
            name="runerrors",
            table="wetlab_run_errors",
        ),
        migrations.AlterModelTable(
            name="runningparameters",
            table="wetlab_running_parameters",
        ),
        migrations.AlterModelTable(
            name="runprocess",
            table="wetlab_run_process",
        ),
        migrations.AlterModelTable(
            name="runstates",
            table="wetlab_run_states",
        ),
        migrations.AlterModelTable(
            name="sambaconnectiondata",
            table="wetlab_samba_connection_data",
        ),
        migrations.AlterModelTable(
            name="samplesinproject",
            table="wetlab_samples_in_project",
        ),
        migrations.AlterModelTable(
            name="statsflsummary",
            table="wetlab_stats_fl_summary",
        ),
        migrations.AlterModelTable(
            name="statslanesummary",
            table="wetlab_stats_lane_summary",
        ),
        migrations.AlterModelTable(
            name="statsrunread",
            table="wetlab_stats_run_read",
        ),
        migrations.AlterModelTable(
            name="statsrunsummary",
            table="wetlab_stats_run_summary",
        ),
        migrations.CreateModel(
            name="LibPrepare",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "lib_prep_code_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "user_sample_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "project_in_samplesheet",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "sample_plate",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("sample_well", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "index_plate_well",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("i7_index_id", models.CharField(blank=True, max_length=25, null=True)),
                ("i7_index", models.CharField(blank=True, max_length=30, null=True)),
                ("i5_index_id", models.CharField(blank=True, max_length=25, null=True)),
                ("i5_index", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "genome_folder",
                    models.CharField(blank=True, max_length=180, null=True),
                ),
                ("manifest", models.CharField(blank=True, max_length=80, null=True)),
                ("reused_number", models.IntegerField(default=0)),
                ("unique_id", models.CharField(blank=True, max_length=16, null=True)),
                (
                    "user_in_samplesheet",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "samplename_in_samplesheet",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "prefix_protocol",
                    models.CharField(blank=True, max_length=25, null=True),
                ),
                (
                    "lib_prep_state",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wetlab.libpreparestates",
                    ),
                ),
                (
                    "molecule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.moleculepreparation",
                    ),
                ),
                ("pools", models.ManyToManyField(blank=True, to="wetlab.LibraryPool")),
                (
                    "protocol_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.protocols",
                    ),
                ),
                (
                    "register_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sample_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.samples",
                    ),
                ),
                (
                    "user_lot_kit_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.userlotcommercialkits",
                    ),
                ),
                (
                    "user_sample_sheet",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wetlab.libusersamplesheet",
                    ),
                ),
            ],
            options={
                "db_table": "wetlab_lib_prepare",
                "ordering": ("lib_prep_code_id",),
            },
        ),
        migrations.AlterField(
            model_name="additionaluserlotkit",
            name="lib_prep_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wetlab.libprepare"
            ),
        ),
        migrations.AlterField(
            model_name="libparametervalue",
            name="library_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wetlab.libprepare"
            ),
        ),
        migrations.DeleteModel(
            name="LibraryPreparation",
        ),
    ]
