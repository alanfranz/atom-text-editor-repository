## Atom Text Editor APT/YUM Mirror
This is my own mirror containing Linux [releases](https://github.com/atom/atom/releases) for [Atom](https://atom.io), the *hackable text editor for the 21st century* . **THIS IS NOT A REBUILD** like other repos around, it's **just an upload of the original packages** for easier install and upgrade. Check the MD5 or the content yourself if you don't trust me.


**WARNING**:Since I don't rebuild such packages, it's upstream developers' responsibility to make them work. They should work on most recent Linuxes, if you find they don't just drop me an email and I'll remove such distro.

I'm not affiliated with GitHub nor Atom developers; I created this mirror for my own consumption, but I think it may be useful to others.

The upload of new packages is automated, and the mirror is usually updated within two hours since official release time.

## This is a repository for stable versions only

I'm not hosting beta releases and I don't plan to, right now (open a ticket if you're really interested); I plan to host stable releases only.

Currently Atom follows a linear development model, a-la-Chrome, so there's just one stable, supported version at one given time; if they choose at a certain point to support multiple stable versions (e.g. 1.x and 2.x) I'll probably split and multiply the repo to let the user choose its preferred version.

## **GOTCHA**: Updating the package while Atom is open

I've found that sometimes updating the package while Atom is open will yield strange issues - e.g. the old process won't die when shutdown (but the GUI **will** disappear - otherwise it would be far too easy to detect an issue) and the new process will try to to start but get locked.

Since I don't rebuild/modify such packages, I cannot change this behaviour; I can just suggest that, if you find that Atom doesn't start after an update, you run a ```killall atom``` command before panicking.

## APT for Debian and Ubuntu
first, fetch Bintray's public key:

```
curl https://www.franzoni.eu/keys/D401AB61.txt | sudo apt-key add -
```

Then, make sure ```apt-transport-https``` is installed;

```
sudo apt-get -y install apt-transport-https
```

And add the following content to ```/etc/apt/sources.list.d/atom.list```

```
deb https://dl.bintray.com/alanfranz/atom-apt stable main
```

Then perform the usual

```
apt-get update
apt-get install atom
```

## YUM for Centos/RHEL and Fedora

Use this repo file, put its in content in ```/etc/yum.repos.d/atom.repo``` and then proceed with a ```yum install atom``` or ```dnf install atom``` as usual:
       
```
[atom]
name=atom
baseurl=https://dl.bintray.com/alanfranz/atom-yum
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://www.franzoni.eu/keys/D401AB61.txt
```

## FAQ

### Why aren't RPM packages signed?

AFAIK upstream RPM packages are unsigned. Since I don't rebuild them and I want them to be unaltered, they're unsigned as well on my repo. By the way the repo itself is signed, so you shouldn't mind about rogue packages being downloaded through an http-only connection.

