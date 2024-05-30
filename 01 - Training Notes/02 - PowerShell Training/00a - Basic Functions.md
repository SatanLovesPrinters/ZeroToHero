```powershell

function Display-Message-1()
{
    [String]$value1 = $args[0]
    [String]$value2 = $args[1]

    Write-Host $value1 $value2
}

function Display-Message-2() 
{

    Param(
        [Parameter(Mandatory=$true)]
        [String]$Text  
    )

    Write-Host $Text

}

function Display-Message-3() 
{

    Param(
        [Parameter(Mandatory=$true)]
        [ValidateSet("Hello World 1","Hello World 2", "Hello World")]
        [String]$Text  
    )

    Write-Host $Text
       
}

```

### Calling a function to be used with Write-Host

```powershell
function Add-FourNumbers (){
    param (
          #Specifies the number list
        [Int32]$first,
        [Int32]$second,
        [Int32]$third,
        [Int32]$fourth     
    )
    
    $result = $first + $second + $third + $fourth

    #Write Sum to Console
Write-Host "$($first) + $($second) + $($third) + $($fourth) = $($result)"
#You can also do Get-Help functionName 

}

```