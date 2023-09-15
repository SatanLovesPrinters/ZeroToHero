## LinkedIn Learning 

| PowerShell 7 Essential Training & Intro to PowerShell 7  | Key Section Information |  Special notes   |
|:------------------|:----------:|:----------:|
| Data Type 1       | filler | string |
| Data Type 2       | filler | string |


| Commands Learned   | Specific Notes   | References   |
| :------------------|:----------:|:----------:|
| Import-Module -ListAvailable  -PSDiagnostics | Add a Pipeline Operator ( &#124; ) to export into next section | [Notes] | [Notes] |



Disable-PSTrace/Enable-PSTrace..+6 more)  to Get-Module -module info
You can actually modify & import only needed functions/cmdlets of modules.	Import-Module
Get-Module
	$module = Import-Module PSDiagnostics
Get-Command *PSTrace*
	
- i.e. Import-Module PSDiagnostics -function Disable-PSTrace, Enable-PSTrace	After you import the module, you add a -prefix on the module & anytime you Get-Module, it will print only that list of active functions/cmdlets imported/not disabled.

$session = New-PSSession - ComputerName PC#1
Get-Module -PSSession $session -ListAvailable -Name PSDiagnostics
Topic: Commands and Syntax	 
Discovering Commands / Exploring Help / Terse Commands	Get-Command -Verb Add / Get-Command -Noun Computer / Get-Command -CommandType Cmdlet
Get-Command -Verb Add / Get-Command -Noun Computer / Get-Command -CommandType Cmdlet Get-Command *event* Find-Command > cmdlets, alises, functions, workflows - Returns a PSGetCommandInfo & you can then pipeline this down.
- VERB / NOUN / CMDLETS / COMMANDS	Get-Command *event* 
- Standardized powershell form is > Verb hyphenated to a Noun	Find-Command > cmdlets, alises, functions, workflows - Returns a PSGetCommandInfo & you can then pipeline this down.
- TERSE COMMANDS



Prints a list of all parameters	Get-Help Format-Table | Out-Host -paging orhelp [cmdlet]
- Gives Name,Syntax,Aliases,Remarks
Get-Help Format-Table Detailed
- (Full or Detailed)
	Get-Help Get-ChildItem -parameter *
- Get-Help	Get-Help about_*  
- Searched online for any cmdlet that starts with "about_"
Get-Help -Name remoting 
	        - gives more details/similar phrases/content
- Variables start with $ i.e. ($_parameterB.count = Import-Csv -…)	Get-Service | Sort-Object -property Status
Get-Member gives methods & properties
Select-Object gives properties but not members.	Get all services, exclude stopped services, show display names only:
Get-Alias or Set-Alias
	Get-Service | WHERE {$_.status -eq 'Running'} | SELECT displayName
You can even pipeline with another | Export-CSV or Out-File "C:\file1"
Variables = $
Terse CMDs = "Format-Table" = 'ft' or Get-Command = gcm
Get-Command | Where-Object { $_.parameterSets.count -gt 2 } | format-list Name
Turns into:
Gcm | ? { $_.parameterSets.count -gt 2 } fl
Write-Output = echo
	
Get-Service | Where-Object { $_.Status }
Get-Service | Where-Object { $_.Status -eq "Running} | Select-Object DisplayName	


PowerShell Objects
Use this when looking for unknown elements of a service	Get-Service -ServiceName 'Dnscache' | Select-Object -Property 'StartType'
i.e. $svcDNSCache = Get-Service -ServiceName 'Dnscache'
- Followed by $svc.Name or $svc.[property]
Get-Service | Get-Member -MemberType 'Method'
- You can utilize this to filter down properties & manually inspect what is happening on a certain process. 
Get-Service -serviceName * | Select-Object -Property 'Status', "DisplayName' | Sort-Object -properrty 'Status' -Descending

</details>

How to improve in my day-to-day?
	- Setup a lab of virtual machines
		○ DC to Member Server to Workstation
		○ Be able to copy a powershell script from domain controller down.
	- Get a list of my administrative duties & see if any can be shortened via PowerShell
	
Summary of Topics: 
	- Advanced-PowerShell-Functions
	- [CmdletBinding()] Param() && PowerShell-Whatif & -Confirm && TXT-vs-CSV-cs-XML
	- Open Arrays /PowerShell-Variable-Storage/Array-Storage / Readdressing of PowerShell-Arrays
		○ Reminder : Elements of an array are stored as $regPowerShellArray.storedElements
		○ $JSONarray = @{}
		○ $regPowerShellArray = @()
		○ Example of $Array.Element Manipulation
$XMLPath = 'C:\Temp\XMLTest.XML"
$ClientList = [xml](Get-Content $XMLPath)
$UserIwantToModify = $ClientList.SetB_Roster.Subset_Employee[2002] #Value in array
$UserIwantToModify.jobTitle="Terminated!" #Even if this value doesn't exist, you will end up creating a new sub element.
		$ClientList.Save($XMLPath) #This will all be for nothing unless you save the file. Everything is stored local until then.
	- Get-Service | ConvertTo-Json | Out-File C:\Temp\jsonTest.json
	- WebInvoke = JSON 
	- REST API 
		
		The basics of pipelining to an element + Advanced-Get-ChildItems:
Get-Command | Where-Object {$_.Name -like '*Invoke*' } #Setting multiple parameters/blocks
		○ Get-Command | Where-Object { () -and/ne/like () }
		
Get-ChildItem & All Directory Functionality 
Set-Location 
	- Allows you to set current directory.
		○ Validate via -PassThru parameter.
		○ = Zero or more
		○ ? = Exactly one character
		○ [] = matches = string must match

Step-by-Step Feature Inclusion of PowerShell's Get-ChildItem
			1. Get-ChildItem C:\ -Name
			2. Get-ChildItem Path C:\Documents\[path] -Recursive -Force
			3. Get-ChildItem -Path $Location -Recurse -Include *.xlsx -Force 
				a. Swap -Include for -Exclude
			4. Get-ChildItem -path $Location -Recurse | Where-Object -FilterScript { ($_.LastWriteTime -eq '2023-01-01') -and (FIELD TWO) }
				a. Get-ChildItem -path $Location -Recurse | Where-Object -FilterScript { (FIELD ONE) -and (FIELD TWO) }
		
		
		New-Item -path "$($Location)\PSFolderNew" -ItemType Directory -Force
		New-Item -path "$($Location)\PSFolderNew\PSFile.txt" -ItemType File -Force
		$document = 'myTestDocument.doc' 
		$document | Out-File -FilePath "$($Location)\PSDocument.txt"
		
		Remove-Item -path "$($Location)\PSDocument.txt\"
		Copy-Item -path "$($Location)\PSDocument.txt\" -Destination "$($Location)\Users\PSDocument-Copy.txt"
		Get-ChildItem "$($Location)\TextFiles\*.txt" | Rename-Item -NewName {$_.Name -replace .\.txt$','.bak' }
		
		
		Import-Csv "$($Location)\Employees.csv" | ForEach-Object 
		        {Write-Host "$($_.FirstName), $($_.LastName) born $($_.DateOfBirth)"}
		
	

How to use: 	Load the function Stop-Everything into PowerShell
Add -Whatif or -Confirm
-Whatif will show what process is going to occur
-Confirm will show you what process is going to occur but then ask for permission
before accessing / changing the data. Confirm will change data, WhatIf will show
all possible impacts of what you are doing.
-whatif & -confirm
        Example
        Function Stop-Everything {
        [CmdletBinding(SupportsShouldProcess)] Param()
                Get-Service * | Stop-Service
        }
Converting to HTML:

<some script> | ConvertTo-HTML | Out-File -path C:\Temp\doc.html
	This allows you to create HTML files that output as a webpage. You can routinely run
reports that allow a web page to be updated "on-the-fly" i.e. Controller Scripting
Txt = White Space
CSV = Punctuation
XML = Markup language / Tables of data	HTML = <table> <tr> <td>
XML = Similar to HTML, but more broken down (<XML Version> <Tag1> <Subtag1>

### XML Data Step-by-Step
```powershell
$XMLPath = 'C:\Temp\XML.xml'
$EmployeeRoster = [XML](Get-Content $XMLPath)
$EmployeeRoster.roster.employee | Format-Table
You can use
$EmployeeRoster.SelectNodes("//name")	Writing to XML Configuration:
$XMLPath = 'C:\Temp\XMLTest.XML'
$EmployeeRoster = [xml](Get-Content $XMLPath)
$EmployeeRoster.roster.employee | Format-Table
- When working with individual users, set them into a variable.
$Bernie = $EmployeeRoster.roster.employee[7] // Check for Bernie with typing $Bernie
Bernie.jobdescription="Landscaping" // To update this information:
$EmployeeRoster.Save($XMLPath) 
/**Save XML File (w/o doing will cause error) & xpath syntax, where any tag related to name will pull**/
$EmployeeRoster.SelectSingleNode ("//employee[4]") 

```
- In XML - the listArray starts @ [1] 
- PowerShell - listArray starts @ [0] 
## XML Data / Advanced Information

- Child Elements of each Primary Element
- How to add a child element into their record:	
- "JavaScript Object Notation" = .JSON
- JSON or XML = Multiple data types, data and objects, and hierarchical structure.
- You can then ADD or REMOVE XML Information. 
Test it: 
```powershell
Get-Service | Export-CLIxml C:\Temp\xmlTest.xml
Get-Service | ConvertTo-Json | Out-File C:\Temp\jsonTest.json
$XMLPath = 'C:\Temp\XMLTest.XML'
$EmployeeRoster = [xml](Get-Content $XMLPath)	
$Bernie = $EmployeeRoster.roster.employee[7]	  
$Bernie.AppendChild($EmployeeRoster.CreateElement("pe_1year"))	
$Bernie.pe_1year = "7/18/2018 Exceeds"
$NewHire = $Bernie.Clone()  //Add a new record (CLONE METHOD)	
$NewHire.Id/Name/JD/DateofHire/EmailAddress = 'value'
$EmployeeRoster.Roster.AppendChild($NewHire)
DO NOT FORGET: $EmployeeRoster.Save($XMLPath)

```   
### XML vs JSON 
XML: Better cmdlet support, more robust 
XML: Normally larger file size than JSON   
XML: More header information & tags to close/open each element
JSON: Sits in between Get-Something | ConvertFrom-Json | Do-Something
JSON: Smaller file, faster web transfer
JSON: Nesting elements, but XML has much better machine level support (e.g) Web-Invoke of REST API

```powershell
Invoke-WebRequest -Method get -URI HTTPS://[siteinformation].com/api/posts/all 
| Select-Object -ExpandProperty Content | ConvertFrom-Json | ft
```

### Utilizing JSON 
```json
Start the script with 
@"
[
 {
    "firstName":"Robert"
}
]
"@ | ConvertFrom-Json | FT

```



