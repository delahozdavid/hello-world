import yaml

# Lista de intents a revisar y modificar
intents_to_check = [
    "account_fixed_transfer",
    "account_fixed_transfer_noworkinghours",
    "account_harddisconnection",
    "account_harddisconnection - go to agent",
    "account_service_transfer",
    "Active Plan - fixed",
    "Active Plan - postpaid",
    "activeplan-fixed - no - transfer",
    "ActivePlan-login-fixed",
    "ActivePlan-login-postpaid",
    "activeplan-postpaid - no - transfer",
    "balance_liberate_transfer",
    "Default Welcome Intent - tech issues - internet - Other",
    "Default Welcome Intent - tech issues - More than one",
    "FAQ - Appointment status",
    "FAQ - Cancel service",
    "FAQ - Damages and Vandalism",
    "FAQ - Flow On Demand - VOD Issues",
    "FAQ - issues with sms",
    "FAQ - Move service",
    "FAQ - No Internet Connection - Home - yes - Other",
    "FAQ - No Internet Connection - MiFi",
    "FAQ - Phone issues - Fixed - Other",
    "FAQ - Reconnection Issues",
    "FAQ - SIM Issues",
    "FAQ - Tech no show",
    "FAQ - Ticket followup - postpaid",
    "FAQ - Ticket followup - prepaid",
    "FAQ - TV issues - Other",
    "FAQ - Update Personal Info",
    "FAQ - WiFi Support - Other",
    "Fault_Installation update",
    "internet_service_payment_cerillion - no - no",
    "internet_service_payment_cerillion - yes - no - no",
    "login_tranfer_mobile",
    "login_transfer_care",
    "paymenthistory - no - yes",
    "paymenthistory-fixed - no - yes",
    "paymenthistory-postpaid - no - yes",
    "paymenthistory-postpaid - yes - Service Issues - no - no",
    "paymenthistory-postpaid - yes - Service Issues - no - yes",
    "rebootcer_failed",
    "rebootcer_success - no",
    "Signal_Service issues - general - More than one",
    "Ticket followup - fixed - assigned - yes",
    "ticketstatusfixed_transfer",
    "Topup Prepaid - Missing Credit",
    "Topup Prepaid - Other Topup Inquiries",
    "Topup Prepaid - Voucher Issues",
    "Transfer to agent - Care",
    "Transfer to agent - Mobile",
    "Transfer to agent - Tech",
    "Transfer_to_Care",
    "Transfer_to_Mobile",
    "Transfer_to_Tech"
]

# Leer el archivo YAML
file_path = 'Lila_Barbados_Prod_v31-0.yaml'
with open(file_path, 'r') as file:
    yaml_data = yaml.safe_load(file)

states = yaml_data.get('inboundShortMessage', {}).get('states', [])

for state in states:
    state_name = state.get('state', {}).get('name', 'Unknown State')
    variables = state.get('state', {}).get('variables', [])
    
if states:
    first_state = states[0]
    state_name = first_state.get('state', {}).get('name', 'Unknown State')
    variables = first_state.get('state', {}).get('variables', [])
    
    print(f"\nFirst State Name: {state_name}")
    
    for variable in variables:
        if 'booleanVariable' in variable:
            boolean_variable = variable['booleanVariable']
            print(f"Boolean VBariable in First State: {boolean_variable}")
            
else:
    print("No states found.")
