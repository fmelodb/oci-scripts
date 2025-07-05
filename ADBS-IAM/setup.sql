
BEGIN
   DBMS_CLOUD_ADMIN.ENABLE_EXTERNAL_AUTHENTICATION( 
      type => 'OCI_IAM' );
END;
/

SELECT NAME, VALUE FROM V$PARAMETER WHERE NAME='identity_provider_type';


-- create a OCI policy
-- Allow group [group] to use autonomous-database-family in compartment [compartment]
-- Allow group [group] to use autonomous-database-family in compartment [compartment] where target.ocid=[database ocid]
-----------


-- iam group / dynamic group
CREATE USER iam_group_app_user IDENTIFIED GLOBALLY AS 'IAM_GROUP_NAME=group_name';   

-- iam user
CREATE USER iam_user_app_user IDENTIFIED GLOBALLY AS 'IAM_PRINCIPAL_NAME=user.name';  

-- instance principal
CREATE USER ip_user IDENTIFIED GLOBALLY AS 'IAM_PRINCIPAL_OCID=ocid1.instance.region1.xxxxx';

-- resource principal
CREATE USER rp_user IDENTIFIED GLOBALLY AS 'IAM_PRINCIPAL_OCID=ocid1.dbsystem.oc1.xxx';

-- create a global role and grant permissions

CREATE ROLE ai_role IDENTIFIED GLOBALLY AS 'IAM_GROUP_NAME=group_name';  

GRANT CREATE SESSION    TO ai_role;
GRANT DB_DEVELOPER_ROLE TO ai_role;
GRANT SELECT ON data_owner.documents TO ai_role;




