## Atom Text Editor APT/YUM Mirror
If you came here for my repos containing [atom releases](https://github.com/atom/atom/releases) (it's not a rebuild, it's just an upload of the original packages for easier upgrade ), Here's your reward.

**WARNING**:Since I don't rebuild such packages, it's upstream developers' responsibility to make them work. They should work on most recent Linuxes, if you find they don't just drop me an email and I'll remove such distro.

I'm not affiliated with GitHub nor Atom developers; I created this mirror for my own consumption, but I think it may be useful to others.

The upload of new packages is automated, and the mirror is usually updated within two hours since official release time.

## APT for Debian and Ubuntu
first, fetch my public key

```
curl https://www.franzoni.eu/keys/D1270819.txt | sudo apt-key add -
```
then, add the proper line in ```/etc/apt/sources.list``` (or add a file in ```/etc/apt/sources.list.d``` with the appropriate content)

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
