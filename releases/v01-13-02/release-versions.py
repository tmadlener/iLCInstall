###########################################
#
# iLCSoft versions for release v01-13-02
#
# F.Gaede, DESY 09.12.2011
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-13-02'
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
ilcsoft_install_prefix = "/scratch/$USER/ilcsoft/"
#ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_dir = os.path.join( ilcsoft_install_prefix, ilcsoft_release )
# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# python variable for referring the ILC Home directory
# used to link or use already installed packages (SL4 or SL5)
# no need to set this variable if using SL4 or SL5 with access to /afs/desy.de/
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/i386_gcc41_sl5/'
#ilcPath = ilcsoft_afs_path[ arch ]
# ----------------------------------------------------------------------------



# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# ----- mysql --------------------------------------------------------
MySQL_version = "5.0.45"
MySQL_path = ilcPath + "/mysql/" + MySQL_version
#MySQL_path = "/usr"


# ----- java ---------------------------------------------------------
Java_version = "1.6.0"
Java_path = ilcPath + "/java/" + Java_version # comment out to try auto-detect


# ----- geant4 -------------------------------------------------------
Geant4_version = "9.4.p03"
Geant4_path = ilcPath + "/geant4/" + Geant4_version
# path to geant4 environment initialization script
# comment out if not needed
G4ENV_INIT_path = ilcPath + "/geant4/" + "env_" + Geant4_version + ".sh"


# ----- CERNLIB ------------------------------------------------------
CERNLIB_version = "2006" 
CERNLIB_path = ilcPath + "/cernlib/" + CERNLIB_version




# ======================= PACKAGE VERSIONS ===================================


ROOT_version = "5.28.00f"

CLHEP_version = "2.1.0.1" 

GSL_version = "1.14"

QT_version = "4.2.2" # mac osx needs version >= 4.7.3

CMake_version = "2.8.5"



# -------------------------------------------

LCIO_version = "v02-00-03" # v02-00-02

GEAR_version = "v01-01"

CED_version = "v01-05" # "v01-04-01"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-5"

ILCUTIL_version = "v00-03"

FastJet_version = "2.4.2"
FastJetClustering_version = "v00-02"
MarlinFastJet_version = "v00-01"


StandardConfig_version = "v03-51-01"
MokkaDBConfig_version = "v03-06"
LCFI_MokkaBasedNets_version = "v00-01" 



# -------------------------------------------

KalTest_version = "v01-04" # "v01-03"

KalDet_version = "v01-05" # "v01-04"

LCCD_version = "v01-02"

RAIDA_version = "v01-06-02"

MarlinUtil_version = "v01-05"

Marlin_version = "v01-02"

Mokka_version = "mokka-07-07-p05"

MarlinReco_version = "v01-00-01" # "v01-00"

MarlinTrk_version = "v01-03" # "v01-02"

MarlinTrkProcessors_version = "v01-02" # "v01-01"

Clupatra_version = "v00-04-01"

LCFIPlus_version = "v00-03"

ForwardTracking_version = "v01-01-01" # v01-01

MarlinKinfit_version = "v00-01"

PandoraPFANew_version = "v00-08"
MarlinPandora_version = "v00-07"
PandoraAnalysis_version = "v00-03"


LCFIVertex_version = "v00-06-01"

CEDViewer_version = "v01-04-01"

Overlay_version = "v00-11-01"

#Eutelescope_version = "v00-06-03"

PathFinder_version =  "v00-01-00"
MarlinTPC_version =  "v00-09-01" # v00-09-00

Druid_version = "1.8" 

Garlic_version = "v2.0.4"

