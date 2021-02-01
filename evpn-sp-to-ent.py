import subprocess
import sys

#################################################################################################################################
# Accetta in input un file di testo che contiene la configurazione delle leaf
# in fornato Service Provider e fornisce in uscita i comandi per trasformarla in formato Enterprise
#
# La configurazione in ingresso e' ottenuta dal comando "show configuration | display set | no-more"
#################################################################################################################################

INVENTORY = []

# tzRoma=timezone(timedelta(hours=1), name='tzRoma')
# print("{:s} - {:s}".format(datetime.now().astimezone(tz=tzRoma).isoformat(), 'Starting ....'))
# print("{:s} - {:s}".format(datetime.now().astimezone(tz=tzRoma).isoformat(), 'Getting management address from VMM'))
#################################################################################################################################
#
# Create list of Vlan with associated VNI
#
#################################################################################################################################

for LINE in open(sys.argv[1]):
  if 'vxlan vni' in LINE:
    NOMEVLAN = LINE.split()[2]
    INVENTORY.append( { 'nomevlan':NOMEVLAN, 'listaifl':[] } )

#################################################################################################################################
#
# Attach ifl to Vlans
#
#################################################################################################################################

for LINE in open(sys.argv[1]):
  if ('set vlans' in LINE) and ('interface' in LINE):
    NOMEVLAN = LINE.split()[2]
    if NOMEVLAN in [nomevlan1['nomevlan'] for nomevlan1 in INVENTORY]:
      NOMEIFL = LINE.split()[4]
      [VLAN1['listaifl'].append(NOMEIFL) for VLAN1 in INVENTORY if VLAN1.get('nomevlan', 0) == NOMEVLAN]

# print(str(INVENTORY).replace("'", '"'))
# print(str(INVENTORY))
# print()

#################################################################################################################################
#
# Delete ifls from Vlans and ifd
#
#################################################################################################################################

for VLAN1 in INVENTORY:
  UNIT=VLAN1['nomevlan'].replace("VLAN-", "")
  for IFL1 in VLAN1['listaifl']:
    IFD = IFL1.split(".")[0]
    print("delete vlans {:s} interface {:s}".format(VLAN1['nomevlan'], IFL1))
    print("delete interfaces {:s} unit {:s}".format(IFD, UNIT))

#################################################################################################################################
#
# Recreate ifd and Vlans
#
#################################################################################################################################

for VLAN1 in INVENTORY:
  UNIT=VLAN1['nomevlan'].replace("VLAN-", "")
  print("set vlans {:s} vlan-id {:s}".format(VLAN1['nomevlan'], UNIT))
  for IFL1 in VLAN1['listaifl']:
    IFD = IFL1.split(".")[0]
    print("set interfaces {:s} unit 0 family ethernet-switching storm-control storm-control-standard".format(IFD))
    print("set interfaces {:s} unit 0 family ethernet-switching interface-mode trunk vlan members {:s}".format(IFD, VLAN1['nomevlan']))


