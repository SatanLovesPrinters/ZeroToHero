```powershell
$a = 0
$b = 1

if ($a -lt $b) {
    $msgOne = "Matches: This is less than."
} else {
    $msgTwo = "Not matched: This is greater than"
}

if ($a -eq $b) {
    $msgThree = "Matches: This is equal to."
} else {
    $msgThree = "Matches: This is equal to."
}

Write-Host $msgOne 
Write-Host $msgTwo 
Write-Host $msgThree

$customObject = [PSCustomObject]@{
"msgOne" = $msgOne
"msgTwo" = $msgTwo
"msgThree" = $msgThree
}
Write-Host $customObject.msgOne

$customTernaryObject = [PSCustomObject]@{
    "msgOne" = ( ($a -gt $b) ?  "Matches: This is less than." : "Not matched: This is greater than")
    "msgTwo" = ( ($a -eq $b) ? "Not matched: This is greater than" : "Not matched: This is greater than")
    "msgThree" = ( ($a -eq $b) ? "Matches: This is equal to." : "Matches: This is equal to.") 
    }
 
    $customObject.msgOne
    

    $value1 = Read-Host "Type favorite Brand"
    $value2 = Read-Host "Type favorite Brand x2"
    Switch ($value1, $value2)
    {
        Brand1 { 'You typed: Brand 1' }
        Brand2 { 'You typed: Brand 2' }
        Brand3 { 'You typed: Brand 3' }
        Brand4 { 'You typed: Brand 4' }
        Brand5 { 'You typed: Brand 5' }
        default {'No value entered'}

    }

```