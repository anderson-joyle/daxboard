***
<i>This project is currently under development. You can find the latest code in DEV branch. Proper instructions on how to use it will be provided once a MVP has been released. Contributions (of any kind) are always welcome.</i>
***

## What is Daxboard?
Daxboard is a "Plug and Play" dashboard for Dynamics 365 FO showing metrics and insights. It communicates with Dynamics 365 FO via REST and Odata.
By design, Daxboard doesn't store any kind of data (credentials or table records).

![daxboard](https://github.com/anderson-joyle/Daxboard/blob/master/screenshot.PNG)

## Motivations
We all know that D365FO has native workspaces, which can be considered dashboards. Native workspaces are well made and work beautifully but contain some limitations (by design):
* Too specific for eassch module. Managers don't have a macro overview of ths system in a single "screen".
* Not mobile friendly.
* (coming soon...)

Daxboard is meant to be:
* Free to use.
* Mobile first.
* Continuosly improved by Dynamics community.
* Development free to D365FO end.

## To whom is Daxboard addressed to?
Daxboard is addressed to be used my directors, managers and support team.
Ideally Daxboard will contain the following dashboards:
* Operations
* Sales
* Inventory
* System administration
* (coming soon...)

## How does it work?
To connect on it, you will need to provide the following arguments into you http request:
* resource - URL to your D365FO e.g.  https://usnconeboxax1aos.cloud.onebox.dynamics.com
* tenant - Azure Active Directory (AAD) domain e.g. contoso.co.uk
* client_id - Application id created Azure Active Directory (AAD) e.g. 8f6a7a48-ee99-4cd4-aedf-a81dee112140
* client_secret - Key which is linked to client id e.g. 65H6A23n48j56d3lAUshkCHU561Be98210d4fDzEGA=

In the end, your URL should looks like this:
https://www.daxboard.com/?resource=<RESOURCE URL>&tenant=<TENANT>&client_id=<CLIENT_ID>&client_scret=<CLIENT_SECRET>


> PS. This approach is rather temporary. There will be a fancy form to log into it.

Stay tunned. More details coming soon...
