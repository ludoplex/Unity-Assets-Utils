# AssetByteTrimmer
## How To Use
- Put the script in the same folder as the assets
- Run the script in command line followed by the mode: `single` or `double` **(required)**
  - `single` is for files with only one Unity header after a few random leading bytes
  - `double` is for files with two Unity header that is only readable after removing all the bytes before the second header
- You can also specify if the old files should be deleted **(optional)**
- You can also specify how long the script should try to search **(optional)**
- You can also specify if the length of the edited file name should be capped **(optional)**
## Notice
- Highly suggest you to read the code first. I'm not responsible for whatever happens to your files.
- Old files are **deleted** by default.
