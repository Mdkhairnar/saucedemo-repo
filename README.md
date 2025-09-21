# saucedemo-repo
Basic UI automation

Tools-->
Behave: BDD framework for writing Gherkin-style test
Selenium library: Web-interface interactions
Python: Assertions
Html reports : behave html formatter

Code structure-->
Feature file allows human readable scenarios
Step definitions allow the code that needs to be executed  
Reports folder stores the html formatted test report 

Execute->
 run via command 'behave' -> stdout shows the execution steps and result
 
 alternate 
 run via command 'behave -f behave_html_formatter:HTMLFormatter -o reports/report.html' -> results stored in reports folder


