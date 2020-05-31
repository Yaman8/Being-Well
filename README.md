Being Well
==========

Our app "Being Well" attempts to minimize the health issues during the lockdown period. As many patients are being neglected ,by the help of our app we can easily contact required health administrations and personnels.

Features
--------
After entering, app contains 5 options which are as follows:
	1. Regular Patients:
		This option is for those who are having health issues apart from the doubt of covid19. A form openes which asks for Name, ID and Cause of Concern. On clicking submit button, a list of hospitals appear from which we can decide the administration to be contacted. On clicking the submit button without any text entered, we have a pop up bar saying "Invalid Entry".
		
	2. Text for Covid:
		Under this thread, we can contact professional authorities for testing covid19. A form opens up here as well asking for Name, Id, Cause and Address. A list of clinics and hospitals are shown where the test can be conducted. The administration can be contacted as wished by the user.
		
	3. COMMUNITY HEALTH:
		For any circumstances in which trained professionals are to be contacted, a list of available health workers are shown. The required worker can be contacted as wished by the user.

	4. MY PROFLE:
		Any required information of user can be changed using my profile option.

	5. MY TICKETS:
		This option displays the bar code of ticket as required for billings.
		
The data entry is stored in two files user.txt and usern.txt.

About
-----
The coding was solely done using Pycharm IDE using kivy library. The project consists of 7 files. Among them 3 are python files, 2 are text files, one is image file and one is kivy file.
The contents are:
	1. main.py
	2. database.py
	3. databasen.py
	4. user.txt
	5. usern.txt
	6. my.kv 
	7. code.png

The "main.py" contains the definition of all the screens and their respective methods. All the screens are navigated using ScreenManager. The "database.py" and "databasen.py" consists of methods of handling data of regular and test for covid19 patients. Similarly, "user.txt" and "usern.txt" stores the data of regular patients and patients who tested for covid19 respectively.The image "code.png" is to simulate a real qr code. Finally, "my.kv" file contains all the codes for styling of buttons and positioning to text. It also gives permission to different screens by the calling of methods. 

Installation
------------
For using the app any python IDE can be user. The IDE should have kivy installed as well. 

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: beingwellnp@gmail.com
