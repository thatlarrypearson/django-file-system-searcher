# Analysis Goals

There were two goals to the [Lightroom Classic Catalog Reader](https://github.com/thatlarrypearson/LightroomClassicCatalogReader), [Django Lightroom Classic Catalog Reader](https://github.com/thatlarrypearson/DjangoLightroomClassicCatalogReader), [File System Searcher](https://github.com/thatlarrypearson/File-System-Searcher) and [Django File System Searcher](https://github.com/thatlarrypearson/Django-File-System-Searcher) projects.

* Find and restore all missing Adobe Lightroom application image files.

* Consolidate the past 20 years of backups into unique files while maintaining a reasonable backup volume and directory structure.

## Image File Recovery

Find and restore all missing Adobe Lightroom application image files.

### Recovery Steps

* Use ```get_file_system``` (see [README](README.md)) on each backup volume (```--volume VOLUME```) using the correct base path (```base_path``` argument).  Do not use ```--no_hash``` as an option as this will make it impossible to differentiate files having the same name.   When there are a number of backups on multiple hard drives this can take time.  In my case, it literally took weeks.

* Use ```get_lr_catalog``` (see [Django Lightroom Classic Catalog Reader](https://github.com/thatlarrypearson/DjangoLightroomClassicCatalogReader)) on each Lightroom catalog including backups.

* Use ```recover_pictures``` (see [Django Lightroom Classic Catalog Reader](https://github.com/thatlarrypearson/DjangoLightroomClassicCatalogReader)).  Choose a ```path``` argument to a large empty hard drive.  Sizing the target drive can be tricky.  In my case, a 4 Terabyte hard drive would be appropriate.

## Backup Consolidation

Consolidate years of backups into unique files while maintaining a reasonable backup volume and directory structure.

### Consolidation Strategy Determination

Getting meaningful results from consolidating backups depends on a number of factors.

* Backup Scope

  Backups can cover whole systems, specific file systems, specific hard drives, home directories, Document directories and so on.  Assume backup scopes to be all over the map.  A hashing algorithm is used to uniquely fingerprint file contents so that duplicate files, regardless of the file name, directory and storage mechanism can be identified.  Selecting the target consolidated directory to place unique files in is easy when little change occurs in directory structures.  Otherwise, directory placement will tend to lack consistency.

* Backup Strategy
  
  Over a period of years, what is backed up and how it was backed up will change.  Directory names where valued files are stored will change.  File naming conventions will change.  Media type file suffixes (e.g. ```.jpg```, ```.jpeg```, etc.) change over time.  Within a set of backups, files will often be duplicated, especially when they have been renamed or moved to another directory location.  

My strategy focuses on recovering __user generated content (UGC)__ and __content__.  UGC is the stuff I create.  Plain old content includes the stuff I created as well as content from other people.  UGC and content both include photos, movies, books, papers, letters, notes, drawings, presentations, spreadsheets, emails and so on.  Windows 10, Linux, Mac OS, programs/applications, log, configuration and etc. files are generally not content.

### Consolidation Steps

* Use ```get_file_system``` (see [README](README.md)) on each backup volume (```--volume VOLUME```) using the correct base path (```base_path``` argument).  Do not use ```--no_hash``` as an option as this will make it impossible to differentiate files having the same name.   When there are a number of backups on multiple hard drives this can take time.  In my case, it literally took weeks.

* The consolidation strategy focuses on content.  Content can be determined by a combination of file suffixes (```suffix```) and mime type (```mime_type```).  With a list of desired file suffixes and another list of desired mime types, consolidation would entail identifying all matching ```dropbox_hash``` and ```size``` files with a matching ```suffix``` __OR__ a matching ```mime_type```.

* Target directory selection can be based decomposing path elements to see what path seems to have to most commonality.  Path commonality cat be determined using the following example.

hostname | volume | file_name | relative_path,full_path | size | dropbox_hash | suffix | mime_type

--------|------|---------|-----------------------|----|------------|------|
widebody | widebody | _MG_9348.CR2,2016\2016-07-02\_MG_9348.CR2,D:\runar\Pictures\2016\2016-07-02\_MG_9348.CR2,
27826813 | 0c245b1e36bd4bbae8b7e931e39781ce01855d9887f965ce69514d2db22121ac | .CR2 | image/CR2
thx-1138 | GCNP-Hiker | _MG_9348.CR2 | Pictures-Recent/Pictures/2016/2016-07-02/_MG_9348.CR2, /media/lbp/GCNP-Hiker/Pictures-Recent/Pictures/2016/2016-07-02/_MG_9348.CR2 | 27826813 | 0c245b1e36bd4bbae8b7e931e39781ce01855d9887f965ce69514d2db22121ac | .CR2 | image/x-canon-cr2
thx-1138 | GlacierNationalPark | _MG_9348 (2019_12_23 21_18_44 UTC).CR2 | trvlbackup-20200103/FileHistory/lbp/WIDEBODY (2)/Data/D/runar/Pictures/2016/2016-07-02/_MG_9348 (2019_12_23 21_18_44 UTC).CR2,
/media/lbp/GlacierNationalPark/trvlbackup-20200103/FileHistory/lbp/WIDEBODY (2)/Data/D/runar/Pictures/2016/2016-07-02/_MG_9348 (2019_12_23 21_18_44 UTC).CR2 | 27826813 | 0c245b1e36bd4bbae8b7e931e39781ce01855d9887f965ce69514d2db22121ac | .CR2 | image/x-canon-cr2
thx-1138 | TRVLBACKUP | _MG_9348 (2019_12_23 21_18_44 UTC).CR2 | FileHistory/lbp/WIDEBODY (2)/Data/D/runar/Pictures/2016/2016-07-02/_MG_9348 (2019_12_23 21_18_44 UTC).CR2, /media/lbp/TRVLBACKUP/FileHistory/lbp/WIDEBODY (2)/Data/D/runar/Pictures/2016/2016-07-02/_MG_9348 (2019_12_23 21_18_44 UTC).CR2 | 27826813 | 0c245b1e36bd4bbae8b7e931e39781ce01855d9887f965ce69514d2db22121ac | .CR2 | image/x-canon-cr2
