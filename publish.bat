py -3 publish.py
cd publish
cd dynamic_mod_menu
Bandizip c -r "dynamic_mod_menu.zip" "*.*"
xcopy "dynamic_mod_menu.zip" "%UserProfile%\Documents\Paradox Interactive\Stellaris\mod" /y
cd .. 
cd ..
cls