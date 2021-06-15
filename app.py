# By Feh's
# V1.0

import PySimpleGUI as sg

import hashlib

import utils.layouts as layouts
import utils.database as database

# vars
title = 'CrudPY'
h = hashlib.sha1()

users = []
clients = []

# Functions
def checkUser(user, pwd):
  h.update(pwd.encode('utf8'))
  password = h.hexdigest()

  info = database.login(user, password)

  if info:
    return info
  else:
    return 'Err'

# Initial Page
loginPage = layouts.loginLayout()

# Events
while[ True ]:
  window, event, values = sg.read_all_windows()

  if event is None and event is sg.WIN_CLOSED:
    break

  if window == loginPage and event == 'btnLogin':
    if values['inputUser'] == '':
      if 'errorPage' in locals():
        errorPage.un_hide()
        errorPage.Element('lblTitle').update('Err: Username is required.')
        errorPage.Element('lblMessage').update('Insert your username.')
      else:
        errorPage = layouts.errorLayout('Err: Username is required.', 'Insert your username.')
    elif values['inputPass'] == '':      
      if 'errorPage' in locals():
        errorPage.un_hide()
        errorPage.Element('lblTitle').update('Err: Password is required.')
        errorPage.Element('lblMessage').update('{} insert your password.'.format(values['inputUser']))
      else:
        errorPage = layouts.errorLayout('Err: Password is required.', 'Insert your password.')
    else:
      confirm = checkUser(values['inputUser'], values['inputPass'])
      
      if confirm == 'Err': 
        if 'errorPage' in locals():
          errorPage.un_hide()
          errorPage.Element('lblTitle').update('Err: Incorrect username or password.')
          errorPage.Element('lblMessage').update('User please check if you entered your data correctly.')
        else:
          errorPage = layouts.errorLayout('Err: Incorrect username or password.', 'User please check if you entered your data correctly.')
      else:
        loginPage.hide()
        dashboardPage = layouts.dashboardLayout(confirm, database.getClients())
        
  if 'errorPage' in locals():
    if window == errorPage and event == 'btnOk':
      break

  if 'dashboardPage' in locals() and window == dashboardPage:
    if event == 'btnCreate':
      dashboardPage.hide()
      createPage = layouts.createLayout()
    if event == 'btnUpdate' and values['tableClient'] != []:
      lists = []
      for client in database.getClients():
        client_id=client[0]
        client_name=client[1]
        client_email=client[2]
        client_phone=client[3]

        lists.append([client_id, client_name, client_email, client_phone])
              
      info = database.getClients(lists[values['tableClient'][0]][0])

      dashboardPage.hide()
      updatePage = layouts.updateLayout(info)
    
    if event == 'btnDelete' and values['tableClient'] != []:
      lists = []
      for client in database.getClients():
        client_id=client[0]
        client_name=client[1]

        lists.append([client_id, client_name])
      
      dashboardPage.hide()
      deletePage = layouts.deleteLayout(lists[values['tableClient'][0]])
    
    if event == 'logout':
      break

  if 'createPage' in locals() and window == createPage:
    if event == 'btnSave':
      name = values['inputName']
      email = values['inputEmail']
      phone = values['inputPhone']

      if name == '':
        createPage.Element("lblAlert").Update(font="Any 8", visible=True)
      if email == '': 
        email = None
      if phone == '': 
        phone = None

      data = database.createClient(name, email, phone)
      dashboardPage.Element("tableClient").Update(data)

      createPage.hide()
      dashboardPage.un_hide()

  if 'updatePage' in locals() and window == updatePage:
    if event == 'btnCancel':
      updatePage.hide()
      dashboardPage.un_hide()

    if event == 'btnSave':
      data = database.updateClient(
        values['inputID'], 
        values['inputName'], 
        values['inputEmail'], 
        values['inputPhone']
      )
      dashboardPage.Element("tableClient").Update(data)

      updatePage.hide()
      dashboardPage.un_hide()

  if 'deletePage' in locals() and window == deletePage:
    if event == 'btnNo':
      deletePage.hide()
      dashboardPage.un_hide()
    if event == 'btnYes':
      deletePage.hide()
      data = database.deleteClient(values['clientId'])
      dashboardPage.Element("tableClient").Update(data)
      dashboardPage.un_hide()
    