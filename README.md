## Atom Text Editor APT/YUM Mirror
This is my own mirror containing [atom releases](https://github.com/atom/atom/releases) .It's not a rebuild, it's just an upload of the original packages for easier upgrade. Check the MD5 or the content yourself if you don't trust me.

**WARNING**:Since I don't rebuild such packages, it's upstream developers' responsibility to make them work. They should work on most recent Linuxes, if you find they don't just drop me an email and I'll remove such distro.

I'm not affiliated with GitHub nor Atom developers; I created this mirror for my own consumption, but I think it may be useful to others.

The upload of new packages is automated, and the mirror is usually updated within two hours since official release time.

## **GOTCHA**: Updating the package while Atom is open

I've found that sometimes updating the package while Atom is open will yield strange issues - e.g. the old process won't die when shutdown (but the GUI **will** disappear - otherwise it would be far too easy to detect an issue) and the new process will try to to start but get locked.

Since I don't rebuild/modify such packages, I cannot change this behaviour; I can just suggest that, if you find that Atom doesn't start after an update, you run a ```killall atom``` command before panicking.

## APT for Debian and Ubuntu
first, fetch my public key by using **either** line from below (uncomment and launch the second if the first fails)

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv D1270819
#curl https://www.franzoni.eu/keys/D1270819.txt | sudo apt-key add -
```


then, add the proper line for your distro and version, as shown below, in ```/etc/apt/sources.list``` (or add a new ```atom-text-editor.list``` file in ```/etc/apt/sources.list.d``` with the same content).

### Ubuntu Precise

```
deb http://www.a9f.eu/apt/atom/ubuntu precise main
```

### Ubuntu Trusty

```
deb http://www.a9f.eu/apt/atom/ubuntu trusty main
```

### Ubuntu Utopic

```
deb http://www.a9f.eu/apt/atom/ubuntu utopic main
```

### Ubuntu Vivid

```
deb http://www.a9f.eu/apt/atom/ubuntu vivid main
```

### Debian Squeeze

```
deb http://www.a9f.eu/apt/atom/debian squeeze main
```

### Debian Wheezy

```
deb http://www.a9f.eu/apt/atom/debian wheezy main
```

### Debian Jessie

```
deb http://www.a9f.eu/apt/atom/debian jessie main
```

## YUM for Centos 7, Fedora 21+

Use those repo files, put their in content in ```/etc/yum.repos.d/atom.repo``` and then proceed with a ```yum install``` as usual:

### Centos 7
```
[atom]
name=atom
baseurl=http://www.a9f.eu/yum/atom/centos/$releasever/$basearch
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://www.franzoni.eu/keys/D1270819.txt
```

### Fedora 21/22/Rawhide:

```
[atom]
name=atom
baseurl=http://www.a9f.eu/yum/atom/fedora/$releasever/$basearch
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://www.franzoni.eu/keys/D1270819.txt
```
