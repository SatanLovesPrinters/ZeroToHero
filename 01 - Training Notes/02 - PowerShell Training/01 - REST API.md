```powershell
<#
Rest API
- Invoke-WebRequest -Method Get
- Rest API documentation will help modifiying the /posts/all site location
- May be something similar to https://[site]/all?user_id=2
#>

#Rest Method
Invoke-RestMethod -Method Get -URI http://examplesiteThatDoesNotExist.com/api/posts/all | Format-Table

```