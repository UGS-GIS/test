import arcpy, time, smtplib

# Set the workspace.
arcpy.env.workspace = r"C:/Users/marthajensen/AppData/Roaming/Esri/Desktop10.8/ArcCatalog/UGHP@ughpadmin@itdb104sp.dts.utah.gov.sde"

# Set a variable for the workspace.
adminConn = arcpy.env.workspace

# Get a list of connected users.
userList = arcpy.ListUsers(adminConn)



# Block new connections to the database.
print("The database is no longer accepting connections")
arcpy.AcceptConnections(adminConn, False)

# Wait 15 minutes.
time.sleep(10)

# Disconnect all users from the database.
print("Disconnecting all users")
arcpy.DisconnectUser(adminConn, "ALL")

# Get a list of versions to pass into the ReconcileVersions tool.
# Only reconcile versions that are children of Default.
print("Compiling a list of versions to reconcile")
verList = arcpy.da.ListVersions(adminConn)
versionList = [ver.name for ver in verList if ver.parentVersionName == 'sde.DEFAULT']

arcpy.ReconcileVersions_management(input_database="C:/Users/marthajensen/AppData/Roaming/Esri/Desktop10.8/ArcCatalog/UGHP@ughpadmin@itdb104sp.dts.utah.gov.sde", reconcile_mode="ALL_VERSIONS", target_version="sde.DEFAULT", edit_versions="UGHPADMIN.Safety", acquire_locks="LOCK_ACQUIRED", abort_if_conflicts="NO_ABORT", conflict_definition="BY_OBJECT", conflict_resolution="FAVOR_EDIT_VERSION", with_post="POST", with_delete="KEEP_VERSION", out_log="", proceed_if_conflicts_not_reviewed="PROCEED", reconcile_checkout_versions="RECONCILE")




# Allow the database to begin accepting connections again.
print("Allow users to connect to the database again")
arcpy.AcceptConnections(adminConn, True)



print("Finished.")