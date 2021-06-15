import PySimpleGUI as sg

title = 'CrudPY'

#         Login         #
def loginLayout():
  layout = [

    [sg.Text('Welcome to CrudPY', font='Any 20', key='lblTitle')],

    [sg.Text('User:', font='10', key='lblUser')],
    [sg.Input(key='inputUser')],

    [sg.Text('Password:', font='10', key='lblPassword')],
    [sg.Input(key='inputPass', password_char='*')],

    [sg.Button('Login', key='btnLogin')],

  ]
  
  return sg.Window('{} - Login'.format(title), layout, finalize=True)

def dashboardLayout(user, clients):
  if clients != None:
    lists = []
    for client in clients:
      client_name=client[1]
      client_email=client[2]
      client_phone=client[3]

      lists.append([client_name, client_email, client_phone])

    headings=["Nome", "E-Mail", "Phone"]

    menus = [
      ['Hello {}!'.format(user[1]), ['logout']]
    ]

    layout = [
      [sg.Menu(menus)],

      [sg.Text('Clients')],

      [sg.Table(values=lists, headings=headings, auto_size_columns=True, justification="center", key="tableClient")],
      [ 
        sg.Button('New', key='btnCreate'), 
        sg.Button('Edit', key='btnUpdate'),
        sg.Button('Delete', key='btnDelete')
      ],
    ]

    return sg.Window(title, layout, finalize=True, auto_size_text=True, auto_size_buttons=True, resizable=True)
  else:
    exit()

#          CRUD          #

def createLayout():
  layout = [
    [sg.Text('Create - Client', font="Any 15", key='lblTitle')],

    [sg.Text('*Name:')],
    [sg.In(key='inputName', change_submits=True)],

    [sg.Text('This field cannot be left blank.', font="Any 8", key='lblAlert', visible=False)],
    
    [sg.Text('E-Mail:')],
    [sg.In(key='inputEmail')],

    [sg.Text('Phone:')],
    [sg.In(key='inputPhone')],
    
    [sg.Button('Cancel', key='btnCancel'), sg.Button('Save', key='btnSave')],
  ]

  return sg.Window(title, layout, finalize=True)

def updateLayout(info):
  print(info)
  layout = [
    [sg.Text(f'Edit - {info[1]}', font="Any 15")],

    [sg.In(info[0], key='inputID', visible=False)], 
    [sg.In(info[1], key='inputName')], 
    [sg.In(info[2], key='inputEmail')],
    [sg.In(info[3], key='inputPhone')],
    
    [sg.Button('Cancel', key='btnCancel'), sg.Button('Save', key='btnSave')],
  ]

  return sg.Window(title, layout, finalize=True)

def deleteLayout(client):
  layout = [
    [sg.Text(f'Delete - {client[1]}', font='Any 15')],

    [sg.In(client[0], visible=False, key="clientId")],

    [sg.Text(f'Are you sure you want to delete the "{client[1]}" client?')],
    
    [sg.Button('No', key="btnNo"), sg.Button('Yes', key="btnYes")]
  ]

  return sg.Window(title, layout, finalize=True)

#         ERRORS         #

def errorLayout(error, message):
  layout = [
    [sg.Text(error, font='any 15', key='lblTitle')],

    [sg.Text(message, key='lblMessage')],
    [sg.Button('Ok', key='btnOk')]
  ]

  return sg.Window('{} - {}'.format(title, error), layout, finalize=True)
