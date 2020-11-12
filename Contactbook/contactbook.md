# Tinku's GUI : The Contact Book

## Overview:
**Contact Book** is a Tinku's GUI made to simulate a pyhton phone book, completely made using procedural programming. In this GUI you can view, delete and updat existing contacts, add a new contact, etc. You are also provided with a help that directs to this page which your seeing right now.

## User Manual:
First run the [*contactbook.py*](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/contactbook.py) and you will see a window called My Contact Book pops up as shown in figure below. At the right corner of the header, you can find today's date. You can find 3 buttons namely view contacts, add contact and help.

| Figure 1: Open the GUI |
| --- |
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/date.png)|

Let's know more about the buttons...

### **_View Contacts_**:
Click the button *view contacts*, a new window(My Contacts) pops up. If you are clicking this window for the first time you will see it is empty as shown below.

- Let's add a new contact using the _Add_ button in the right side of the blank box. 
  - **Add** :  
    - To add a new contact you have to click this button ( or the Add Contact button ).
    - It will open a new window as shown below where you will fill in all the required details and then hit *Add Contact* button which will add the contact to the contact book.

| Figure 2: Hit the add button | Figure 3: Add new contact |
| --- | --- |
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/view.png) | ![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/add.png)|


- To check the details of existing contact use the display button shown below.
  - **Display** :
    - Open _My Contacts_ window if it's not, then select the contact that you want to display the details.
    - Then hit the _Display_ button in the right side of the window.
    - You will se a window(Contact Details) pops up showing the details of the contact selected as shown below.
 
| Figure 4: Hit the display button | Figure 5: Display the existing contact |
| --- | --- |
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/view_2.png) | ![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/disply.png)|


- To update an existing contact, click on the update button as shown below.
  - **Update** :
    - When you hit the update button a window(Update Contact) pops up, filling all the details of the contact that you selected.
    - You can edit the contcat as you widh and then hit the _update contact_ button. 
    - And when you hit it, you will see a message pops showing that the message is sucessfully updated.

| Figure 6: Hit the update button | Figure 7: Update the existing contact |
| --- | --- |
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/view_3.png) | ![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/updt.png)|

Now, let's display the DarlaJones that we just updated.(check out above how display button works)

| Figure 8: Display the updated contact |
| --- |
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/disply_2.png)|

- Let's delete the contact we just created as shown below.
  - **Delete** :
    - Select the contact you want to delete and hit the button _Delete_.
    - Then you will get a pop up asking that "Are you sure, you wanna to delete '_name_'?".
    - If you hit _yes_, then the contact will be deleted and a message appears saying "Contact Deleted".
    - if you hit _no_, then the database remains the same and no  contact will be deleted.
    
| Figure 9: Hit the Deleted button | Figure 10: Delete the existing contact | Figure 11: Database with contact deleted |
| --- | --- | --- | 
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/del.png)|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/del_2.png)|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/del_3.png)


Ok, so far so good we have added a new contact , displayed its details, updated it and also deleted it.

Let's create a bunch of contact using the [data.py](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data.py):

- **Database** :
  - Firstly you have to delete _mycontacts.db_ if it exists in your directory.
  - Then run the file _data.py_, you will see a "sucessfully updated" in the output window.
  - Now run the _contacts.py_ file and open *_View Contacts_* window. You can see a lot of [fake contacts](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/fake_data/dataNov-7-2020.json) there as shown below.
  - You can see that there are only **26** contacts displayed. Inorder to see more contacts, use the scroll bar in the right side of the list box as shown below.
   
| Figure 12: Adding fake contacts to the database | Figure 13: Using the scrollbar | 
| --- | --- |
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set.png)| ![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set_2.png)| 


Let's just perform some operations with the database we just created (as we already know how to do I'm not talking about the process here)

| Figure 14: Updating *_Paki Foster_* | Figure 15: Initial Update Window | Figure 16: Updating the contact| 
| --- | --- | --- |
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set_3.png)| ![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set_4.png)| ![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set_5.png)|

| Figure 17: Display new *_Paki Foster_* | Figure 18: Display the contact| 
| --- | --- |
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set_6.png)| ![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set_7.png)|


So the main point that I wanna point out here, If you have seen that whenever we use these buttons they turn grey and they won't work. Here comes the _Reset_ button.

**Reset** :
  - As you see here, the _Update_ and _Display_ buttons are greyed out 
  - Press the *_Reset_* button and then a window pops up asking you if you want to really enable the buttons ( make sure you really need to)
  - Press _"yes"_ to reset the button's state.
  - Note that the reset is created only to prevent the unnecessary pop up of windows. so, make sure that you don't have duplicate windows.
  - You can also use the reset button to reset the buttons in _My Contcats_ window.
  
| Figure 19: Resetting all the buttons | Figure 20: Buttons greyed up | Figure 21: Reset all the buttons |
| --- | --- | --- | 
|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set_8.png)|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set_9.png)|![](https://github.com/3D-soul/FirstFifty/blob/master/Contactbook/data/figures/set_10.png)|



## Conclusions:

## Final Credits and Notes:
The base project idea is taken from a blog post by Rohit Sharma called [42 Exciting Python Project Ideas & Topics for Beginners]( https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/) and also the youtube playlist [Python GUI tutotrials using tkinter]( https://www.youtube.com/playlist?list=PLjC8JXsSUrri0XWbCGffJ5to1P40hebu2)
