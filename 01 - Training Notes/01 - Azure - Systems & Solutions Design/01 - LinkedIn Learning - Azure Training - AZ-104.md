# Zero to Hero > 01 - Training Notes
## 01 - Training Notes > 01 - Azure - Systems & Solutions Design

| 1| 2 | 3 | 4 | 5 | 6 | 7 |
| :----| :------- | :--- | :--- | :--- | :--- | :--- |
| | | | | | |

## LinkedIn Learning - AZ-104 

[Microsoft Pre-Requisite & Recommended Pathways](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/)

| Sections | Microsoft Pathway Link | Unit(~Hr) |
| :----| :------- | :-------: |
| Identity & Governance | [AZ-104: MS Path](https://learn.microsoft.com/en-us/training/paths/az-104-manage-identities-governance/)       | 1.0 |
| Storage Accounts | [AZ-104: Implement & Manage Storage](https://learn.microsoft.com/en-us/training/paths/az-104-manage-storage/)                         | 1.0 |
| Deploy and Manage Compute Resources | [AZ-104: Deploy & Manage Compute Resources](https://learn.microsoft.com/en-us/training/paths/az-104-manage-compute-resources/)      | 2.0 |
| Configure and Manage Virtual Networking | [AZ-104: Manage Virtual Networks](https://learn.microsoft.com/en-us/training/paths/az-104-manage-virtual-networks/)  | 2.5 |
| Monitor and Maintain Azure Resources | [AZ-104: Monitoring](https://learn.microsoft.com/en-us/training/paths/az-104-monitor-backup-resources/)    | 0.5 |
| Exam Tips (AZ-104) | AZ-104 | 1.0 |
**Total** ~8-8.5 Unit Hours

```Brief Overview
Manage the following: 

Azure AD Objects, Subscriptions & Governance, Storage Accounts, Azure App Services, Docker Containers, Azure VMs, Virtual Networks+Monitoring+Configuration, BCDR/VM Backups + Recovery, Load Balancing, Azure Networking Services, Azure Monitor
```

### Manage Azure Active Directory Objects

| Manage Azure Active Directory Objects  | Summary |
| :----| :-------|
| Manage User & Guest Accounts | |
| Bulk User Updates | |
| Manage Devices | |
| Configuring SSPR | |

#### What is Azure AD?
```
- Multi Tenant
- Identity Management Directory : +User login Authentication, +Azure resources secured with Azure AD accounts
- Azure AD = Trusted provider
- OpenID, OAUTH, SAML / Simplified SSO for Cloud App integration
- Azure AD has multiple configurations (On-Prem/Cloud Only/Hybrid/Federated)
```
- Commonly seen with Azure AD syncing with Active Directory Domain Services (ADDS) & configured/coupled with SSPR/Writeback/Federation/etc.
- Azure AD Custom Domains
    - Custom domain names: Add TXT record from domain provider / host provider inside Azure AD Tenant.
    - Setup custom domain before adding users in. 
- Guests : Can belong to any security role & can be invited by e-mail. 
- Groups : Security Groups & Microsoft 365 Groups
    - Add a GROUP Account to organize users by department, job title, etc.
    - Users and Guests can be in multiple groups
    - Resources can be assigned to Users **and** Groups
- Group Type - Security Group: 
    - **Secures Resources**
    - Add users, groups, or even devices as members to the SG.
- Group Type - Microsoft365 Group:
    - Used for shared mailbox / shared calendar 
    - SharePoint Collection / etc.

- Group Membership Type: Dynamic User / Dynamic Device
    - Requires Azure AD Premium P1
    - Membership is assigned automatically based on up to 5 elements/attributes.
        - Configure Rules : "Property" + "Operator" + "Value" 

#### Bulk Create Options
- Download CSV templates from portal
- Invite guests, Delete, Download
- Download / Import  / Remove members from a group in Azure Directory