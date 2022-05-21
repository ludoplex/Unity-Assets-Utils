# AssetByteTrimmer
- Put the file in the folder of the assets
- Run the script with specified mode: **single** or **double** (required)
- **Single** is for files with only one Unity header after a few random leading bytes
- **Double** is for files with two Unity header that is only readable after remove all the bytes before the second header
- You can also specify if the old files should be deleted (optional)
- You can also specify how long the script should try to search (optional)
- You can also specify if the length of the edited file name should be capped (optional)
