PROMPT executing ADMINCONS_2772_UPDATE_CARBON_DATA.sql by Renuha

update ids_t_report_column set column_display='OLD CARBON-DIRECT+FIRST TIER INDIRECT (TONNES CO2E)' where column_id=166 and report_id=2137;

update ids_t_report_column set column_display='CARBON-DIRECT+FIRST TIER INDIRECT (TONNES CO2E) CHANGE' where column_id=168 and report_id=2137;

update IDS_T_REP_FILE_TYPE_TEMPLATE set column_display='OLD CARBON-DIRECT+FIRST TIER INDIRECT (TONNES CO2E)' where report_file_rel_id=134 and column_order=23;

update IDS_T_REP_FILE_TYPE_TEMPLATE set column_display='CARBON-DIRECT+FIRST TIER INDIRECT (TONNES CO2E) CHANGE' where report_file_rel_id=134 and column_order=25;
commit;

