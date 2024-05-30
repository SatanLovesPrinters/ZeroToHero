```powershell
$jsonObject = @{}
$jsonObject
$arrayList = New-Object System.Collections.ArrayList
$arrayList.Add(@{"Name"="Antonio";"Surname"="Pina";"Gender"="M";})
$arrayList.Add(@{"Name"="Antonio-2";"Surname"="Pina-2";"Gender"="M2";})
$arrayList.Add(@{"Name"="Antonio-3";"Surname"="Pina-3";"Gender"="M3";})
$arrayList.Add(@{"Name"="Antonio-4";"Surname"="Pina-4";"Gender"="M4";})

$employees = @{"Employees"=$arrayList;}

```