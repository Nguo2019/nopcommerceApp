pytest -s -v -m "sanity" --html=./Reports/marker.html testCasespackage/ 
rem pytest -s -v -m "sanity or regression" --html=./Reports/marker.html testCasespackage/ --browser firefox
rem pytest -s -v -m "sanity and regression" --html=./Reports/marker.html testCasespackage/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/marker.html testCasespackage/ --browser chrome
  
##rem means ignore this command. 
 