## HTACCESS file generator

Need a quick error code generator for your apache server ?
Have all your error files stored in one single file ?

This python script generates all the most common http error codes supported by apache2 web server.

 `ErrorDocument 100 /error.html` , `ErrorDocument 101 /error.html`, `ErrorDocument 102 /error.html`



### Instructions 

```python3
1. Generate htacess codes.

2. View library of codes.

0. View Menu.

C. Exit
```



To generate htaccess error codes, select option one.

```python3
>1
write your general html file name (or full path) to generate htaccess.
```



Input your {error_page}.html

```python3
> error_page.html

Generated ! It begins like this :

ErrorDocument 100 /error_page.html

ErrorDocument 101 /error_page.html

ErrorDocument 102 /error_page....

Your output has been copied to your clipboard.
```



Congratulations. Now you have your error code copied to your clipboard.



#### Python lib prerequisites : 

`os`, `pyperclip`

