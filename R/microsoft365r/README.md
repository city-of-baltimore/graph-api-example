# R Package: `Microsoft365R`

<!-- TOC -->

- [R Package: `Microsoft365R`](#r-package-microsoft365r)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Authentication](#authentication)
    - [Get access on behalf of a user](#get-access-on-behalf-of-a-user)
    - [Get access without a user](#get-access-without-a-user)
  - [SharePoint Sites and Lists](#sharepoint-sites-and-lists)
    - [Site Resource](#site-resource)
    - [List Resource](#list-resource)
    - [ListItem Resource](#listitem-resource)
    - [Sharepoint Documents](#sharepoint-documents)
  - [Drives and Files](#drives-and-files)
    - [Drive Resource](#drive-resource)
    - [DriveItem Resource](#driveitem-resource)

<!-- /TOC -->

## Getting Started

### Prerequisites

Contact BCIT with your plans. If you're using a client method, you'll need an app ID and secret created by BCIT. They will need to know what you plan to do with your app and in what SharePoint sites.

### Installation

The usual package installation for `Microsoft365R`. These instructions will also use `AzureGraph` for logging on. See [Microsoft365R](https://github.com/Azure/Microsoft365R) and [AzureGraph](https://github.com/Azure/AzureGraph) for list of dependency details.

## Authentication

### Get access on behalf of a user

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}


### Get access without a user

This is by far the best method if you are want to access SharePoint data in a script or app. In `azureGraph` and `Microsoft365R`, this access method is called the `client_credentials flow`. The ID and secret from BCIT should be stored as environment variables then referenced in the script/app. Other methods may prompt you to log in using a web browser. This method with give auth to an app, thus the app is permissioned to particulate sites and functions.

1. Get app ID and secret from BCIT
1. Save those as environment variables


   You should never store secrets in your code. Instead save them to the `.Reviron` file that should never be in any git commit. Here are two ways to do this:

   In Rstudio:

   ```R
   usethis::edit_r_environ()

   ### this triggers a file to pop up. In the .Renvion that pops up 
   ### add your secret in this format, no quotes or spaces needed

   azure_app_id=zzzz1234appID
   azure_graph_secret=Ade2365645fgdfg

   ```

   In Linux or Mac:

   ```bash
   ## in terminal using the nano editor

   cd ~
   nano .Renviron

   ### add environmental variables like above and save

   ```


   Save changes and restart R. Now you can use `Sys.getenv("azure_app_id")` in the code. Voila, no secrets in your code.


1. Create login

   Use those secrets create a login client to authenticate with Microsoft Graph:

   ```R
   gr <- azureGraph::create_graph_login(tenant = "bmore", 
                         app=Sys.getenv("azure_app_id"), 
                         password=Sys.getenv("azure_graph_secret"))


   ### did it work?
   azureGraph::list_graph_logins()


   ```

1. You're now connected and can use the resultant `gr` object for a number of functions. So far we've used `azureGraph` to create the connection. Now we'll switch over to `Microsoft365R` for reading and writing of data.

## SharePoint Sites and Lists

See code chunks below for data read/write examples

### Site Resource

```R
#### connect to sharepoint site 'MORP' on city tenent
### this connection can be used for both sharepoint lists and files

con_to_sharepoint <- gr$get_sharepoint_site(site_url = "https://bmore.sharepoint.com/sites/MORP")

con_to_sharepoint ### shows functions that can be used with the sharepoint connection

```

### List Resource

```R
#### connect to sharepoint list called 'test_demo'

con_to_sharepoint$get_list("test_demo") ### shows functions that can be performed

con_to_sharepoint$get_list("test_demo")$list_items()  ### reads sharepoint list as dataframe!

#### write to Sharepoint; fields need to match the sharepoint list
con_to_sharepoint$get_list("test_demo")$create_item( Title = "some title",  
                     email = "boaty@mcboatface.ship",  
                     uploadtime = Sys.time(),
                     measurement = "very good")
                     
```

### ListItem Resource

```R
## See list of functions for sharepoint list called 'test_demo'

con_to_sharepoint$get_list("test_demo") 
```

### Sharepoint Documents

Documents saved on sharepoint can be read, created, and edited.

```R
### connect to sharepoint documents
drv <- con_to_sharepoint$get_drive() 

### a couple examples of what you can do

drv$list_files()  ## lists all the files in the documents collection
drv$create_folder("new_folder") ### create a new folder
drv$upload_file("some_local_file.csv", "new_folder/some_local_file.csv") ## writes file. This assumes the file is in the cwd 

```


## Drives and Files

### Drive Resource

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->

### DriveItem Resource

{1-2 sentence summary of this use case}

1. {Step 1 to complete use case}
1. {Step 2 to complete use case}
1. ... <!-- number of steps and use cases may vary -->
