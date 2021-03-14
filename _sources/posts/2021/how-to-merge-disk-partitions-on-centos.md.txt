---
author: Anderson Banihirwe
date: 2021-01-07
tags: todayilearned, linux, centos
---

# How to merge two or more disk partitions on Centos 7

I've been working with centos 7 virtual machine provisioned via VMware's vrealize suite. One thing I particulary dislike is how the storage disk gets partitioned into tiny partititions during the VM provisioning:

```bash
$ df -h
Filesystem                                            Size  Used Avail Use% Mounted on
devtmpfs                                              1.9G     0  1.9G   0% /dev
tmpfs                                                 1.9G     0  1.9G   0% /dev/shm
tmpfs                                                 1.9G  8.9M  1.9G   1% /run
tmpfs                                                 1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-root       6.0G   70M  6.0G   2% /
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-usr        6.0G  1.5G  4.6G  24% /usr
/dev/sda1                                            1014M  232M  783M  23% /boot
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-data        61G   34M   61G   1% /data
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-usr_local  6.0G   33M  6.0G   1% /usr/local
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-home        10G   33M   10G   1% /home
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-var        6.0G  414M  5.6G   7% /var
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-tmp        2.0G   33M  2.0G   2% /tmp
tmpfs                                                 379M     0  379M   0% /run/user/1001
```

Notice how `var`, `data`, `home`, `tmp`, `usr`, `usr_local`, and `root` have their own partitions. I prefer to have a few but large disk partitions. So, today I figured out how to merge two or more partitions into the root partition (thank you, @kmpaul for the help and documenting this!).

## Step 1 — Make sure you are logged in as root

## Step 2 — Backup data from the partitions you want to merge into the root partiton

```bash
$ rsync -a /home/ /home-old/
$ rsync -a /tmp/ /tmp-old/
$ rsync -a /var/ /var-old/
```

## Step 3 — Reboot the VM into an emergency mode

```bash
$ systemctl emergency
```

## Step 4 — Umount and remove logic volume for each of the partitions

```bash
$ umount /dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-data
$ umount /dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-home
$ umount /dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-var
$ umount /dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-tmp
```

```bash
$ lvremove /dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-data
$ lvremove /dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-home
$ lvremove /dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-var
$ lvremove /dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-tmp
```

## Step 5 — Copy the backed up data

```bash
$ rsync -a /home-old/ /home/
$ rsync -a /var-old/ /var/
$ rsync -a /tmp-old/ /tmp/
```

## Step 6 — Edit the `/etc/fstab` file by removing or commenting out the partitions we don't need

```bash
$ vi /etc/fstab
```

## Step 7 — Extend the root partition to fill the remaining space

```bash
$ lvextend -l +100%FREE -r /dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-root
```

## Step 8 — Remove the backups

```bash
$ rm -rf /home-old/ /tmp-old/ /var-old/
```

## Step 9 — Reboot the system

```bash
$ reboot
```

## Step 10 — Login to the VM as a regular user or root

Let's check that our `/` root partition size has increased:

```bash
$ df -h
Filesystem                                            Size  Used Avail Use% Mounted on
devtmpfs                                              1.9G     0  1.9G   0% /dev
tmpfs                                                 1.9G     0  1.9G   0% /dev/shm
tmpfs                                                 1.9G  8.9M  1.9G   1% /run
tmpfs                                                 1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-root        85G  474M   85G   1% /
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-usr        6.0G  1.5G  4.6G  24% /usr
/dev/sda1                                            1014M  232M  783M  23% /boot
/dev/mapper/centos_dhcp--zzz--zzz--zzz--zz-usr_local  6.0G   33M  6.0G   1% /usr/local
tmpfs                                                 379M     0  379M   0% /run/user/1001
```

Voilà! 🙌
