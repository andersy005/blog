---
date: 2021-01-07
category: todayilearned, linux, centos
---

# How to merge two or more disk partitions on Centos 7

I have been working with centos 7 virtual machines provisioned via VMware's vrealize suite. One thing I particulary dislike is how the disk gets partitioned into tiny partititions during the VM provision:

```bash
[admin@dokku ~]$ sudo lsblk
NAME                                         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                                            8:0    0   50G  0 disk
├─sda1                                         8:1    0    1G  0 part /boot
└─sda2                                         8:2    0   49G  0 part
  ├─centos_dhcp--zzz--zzz-zzz-zz-root      253:0    0    6G  0 lvm  /
  ├─centos_dhcp--zzz--zzz-zzz-zz-swap      253:1    0    2G  0 lvm  [SWAP]
  ├─centos_dhcp--zzz--zzz-zzz-zz-usr       253:2    0    6G  0 lvm  /usr
  ├─centos_dhcp--zzz--zzz-zzz-zz-var       253:3    0    6G  0 lvm  /var
  ├─centos_dhcp--zzz--zzz-zzz-zz-home      253:4    0   10G  0 lvm  /home
  ├─centos_dhcp--zzz--zzz-zzz-zz-usr_local 253:5    0    6G  0 lvm  /usr/local
  ├─centos_dhcp--zzz--zzz-zzz-zz-tmp       253:6    0    2G  0 lvm  /tmp
  └─centos_dhcp--zzz--zzz-zzz-zz-data      253:7    0   61G  0 lvm  /data
sdb                                            8:16   0   50G  0 disk
└─sdb1                                         8:17   0   50G  0 part
  └─centos_dhcp--zzz--zzz-zzz-zz-data      253:7    0   61G  0 lvm  /data
sr0                                           11:0    1 1024M  0 rom
```

Notice how `var`, `data`, `home`, `tmp`, `usr`, `usr_local`, and `root` have their own partitions. I prefer to have one or two big disk partitions. So, today I figured out how to merge two or more partitions into a single partition in **three** steps. For instance, here's how I managed to merge the `data` partition into `root`.

## Step 1: Unmount the `data` partition

```bash
[admin@dokku ~]$ sudo umount /dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-data
[admin@dokku ~]$ df -h
Filesystem                                            Size  Used Avail Use% Mounted on
devtmpfs                                              1.9G     0  1.9G   0% /dev
tmpfs                                                 1.9G     0  1.9G   0% /dev/shm
tmpfs                                                 1.9G  8.9M  1.9G   1% /run
tmpfs                                                 1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-root       6.0G   70M  6.0G   2% /
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-usr        6.0G  1.5G  4.6G  24% /usr
/dev/sda1                                            1014M  232M  783M  23% /boot
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-usr_local  6.0G   33M  6.0G   1% /usr/local
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-var        6.0G  416M  5.6G   7% /var
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-home        10G   33M   10G   1% /home
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-tmp        2.0G   33M  2.0G   2% /tmp
tmpfs                                                 379M     0  379M   0% /run/user/1001
```

## Step 2: Remove the `data` logical volume using `lvremove`

```bash
[admin@dokku ~]$ sudo lvremove /dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-data
Do you really want to remove active logical volume centos_dhcp-zzz-zzz-zzz-zz/data? [y/n]: y
  Logical volume "data" successfully removed
```

## Step 3: Extend the `root` volume using `lvextend`

```bash
[admin@dokku ~]$ sudo lvextend -l +100%FREE -r /dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-root
  Size of logical volume centos_dhcp-zzz-zzz-zzz-zz/root changed from 6.00 GiB (1536 extents) to 66.99 GiB (17150 extents).
  Logical volume centos_dhcp-zzz-zzz-zzz-zz/root successfully resized.
meta-data=/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-root isize=512    agcount=4, agsize=393216 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0 spinodes=0
data     =                       bsize=4096   blocks=1572864, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal               bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 1572864 to 17561600
```

## Voilà

Let's check that our `/` root partition size has increased:

```bash
[admin@dokku ~]$ df -h
Filesystem                                            Size  Used Avail Use% Mounted on
devtmpfs                                              1.9G     0  1.9G   0% /dev
tmpfs                                                 1.9G     0  1.9G   0% /dev/shm
tmpfs                                                 1.9G  8.9M  1.9G   1% /run
tmpfs                                                 1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-root        67G   72M   67G   1% /
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-usr        6.0G  1.5G  4.6G  24% /usr
/dev/sda1                                            1014M  232M  783M  23% /boot
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-usr_local  6.0G   33M  6.0G   1% /usr/local
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-var        6.0G  417M  5.6G   7% /var
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-home        10G   33M   10G   1% /home
/dev/mapper/centos_dhcp--zzz--zzz-zzz-zz-tmp        2.0G   33M  2.0G   2% /tmp
tmpfs                                                 379M     0  379M   0% /run/user/1001
```
