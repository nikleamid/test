# У меня есть вот такой код до этого. Получение Json:
payload = {
    "jsonrpc": "2.0",
    "method": "event.get",
    "params": {
        "output": "extend",
        "time_from": f,
        "time_till": g,
        #         "severities": '5'
    },
    "id": 2,
    "auth": AUTHTOKEN
}
events = requests.post(
    ZABBIX_API_URL, data=json.dumps(payload), headers=headers)
events = events.json()['result']


class ReportItem(object):
    id = ""
    start = ""
    end = ""
    name = ""
    severity = ""


def make_reportItem(id, start, name, severity):
    reportItem = ReportItem()
    reportItem.id = id
    reportItem.start = start
    reportItem.name = name
    reportItem.severity = severity
    return reportItem


inputValues = [
    {'eventid_start': '111111', 'time': '123123', 'name': 'test1',
        'eventid_end': '222222', 'severity': '5'},
    {'eventid_start': '333333', 'time': '123456',
        'name': 'test1', 'eventid_end': '444444'},
    {'eventid_start': '222222', 'time': '654321',
        'name': 'test1', 'eventid_end': '0', 'severity': '0'},
    {'eventid_start': '555555', 'time': '765443',
        'name': 'test1', 'eventid_end': '666666'},
    {'eventid_start': '444444', 'time': '435435',
        'name': 'test1', 'eventid_end': '0'},
    {'eventid_start': '777777', 'time': '255455',
        'name': 'test1', 'eventid_end': '888888'},
    {'eventid_start': '666666', 'time': '985498',
        'name': 'test1', 'eventid_end': '0'},
    {'eventid_start': '888888', 'time': '458985',
        'name': 'test1', 'eventid_end': '0'},
    {'eventid_start': '999', 'time': '76876876',
        'name': 'test1', 'eventid_end': '234534'},
]

reportItems = {}
for item in inputValues:
    itemStart = item['eventid_start']
    if (itemStart in reportItems):
        reportItems[itemStart].end = item['time']
    else:
        reportItems[item['eventid_end']] = make_reportItem(
            itemStart, item['time'], item['name'], item.get("severity", ""))

for reportItemKey in reportItems:
    item = reportItems[reportItemKey]
    logMessage = f"id: {item.id}, start: {item.start}, end: {item.end}, severity: {item.severity}"
    print(logMessage)
