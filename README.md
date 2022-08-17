# CryptoSafe

## What's `CryptoSafe` ?

`CryptoSafe` is a **password manager** developed with the `Python` programing language. He is completely **open source** and **free**. **CryptoSafe works only on** `Linux` **based systems** but a `Windows` version **should appears soon**.

## How does it work ?

`CryptoSafe` works with **2 encryption types**. The first one is used for the **master password** which is the main password of your account. The second one is used for **all of your registered password(s)** in your account. `CryptoSafe` have an account system, **it means that you will be able to create multiple accounts** to store your password(s). All of the data about the password(s) **is stocked on your computer** and the **program don't have to connect himself on Internet to work**.

## How to use it ?

* **Clone** the `repository` with this command :
``` bash
git clone https://github.com/MelCaillasse/CryptoSafe
```
* Go into the `CryptoSafe directory` and **install all required modules** with this command :
``` bash
pip3 install -r requirements.txt
```
* And now you just have to **execute the bash script** with this command :
``` bash
./CryptoSafe
```
* or with this command :
```bash
bash CryptoSafe.sh
```
You can now type the `help` command **to display the command list**.

----

## How do I fix **issues** ?

A lot of issues can appear and you can't always know how to fix it. I will explain the main issues which are very simple to fix :

* ### **Execution path error**

The first issue is the execution path issue which isn't display when the error occure.

**So how to fix it ?**

This issue is very simple to fix. The error come from the `execution path` it means that **the error occure when you execute the script from a subdirectory of the** `CryptoSafe.sh` **script**. The simple thing that you have to do is **execute the script from de directory which contains** `CryptoSafe.sh`**.**

* ### **Execution script error**

This issues can only come **if you execute the wrong script**.

**So how to fix it ?**

This issues **come from the script which you execute to start** `CryptoSafe`**.** To avoid it **you have to execute the** `CryptoSafe.sh` **and not the** `Python` **scripts which are in the** `src` **directory.**

* ### **Missing modules error**

This issues occure **if you don't have the** `Python required modules` for the `CryptoSafe scripts` which are in the `src` directory.

**So how to fix it ?**

**You just need to go into the** `CryptoSafe directory` **which contains a file called** `requirements.txt`**.** **After execute this command** :

``` bash
pip3 install -r requirements.txt
```

This command **will install all the** `required modules` which are missing.

----

### If you need help for an other error, you can ask me a question about the error on GitHub...

### **Thank for you download, hope you enjoy !**

## Links :

**GitHub profil : [https://github.com/MelCaillasse](https://github.com/MelCaillasse)**

**GitHub repository : [https://github.com/MelCaillasse/CryptoSafe](https://github.com/MelCaillasse/CryptoSafe)**

**GitHub issues section : [https://github.com/MelCaillasse/CryptoSafe/issues](https://github.com/MelCaillasse/CryptoSafe/issues)**