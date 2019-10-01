.. _osism-ubuntu-preseed:

### Localization

# Preseeding language, country and locale
d-i debian-installer/locale string en_US.UTF-8

# Keyboard selection

# Disable automatic (interactive) keymap detection.
d-i console-setup/ask_detect boolean false
d-i keyboard-configuration/xkb-keymap string us

### Network configuration

# Skip network configuration
d-i netcfg/enable boolean false
# Set hostname and domain
d-i netcfg/get_hostname string ubuntu-host
d-i netcfg/get_domain string osism.customer
# Disable that annoying WEP key dialog.
d-i netcfg/wireless_wep string

### Missing drivers and firmware

d-i hw-detect/load_firmware boolean true

### Mirror
d-i mirror/http/proxy string

### Account setup

# Skip creation of a root account
d-i passwd/root-login boolean false
d-i passwd/make-user boolean true
# User ubuntu with password
d-i passwd/user-fullname string ubuntu
d-i passwd/username string ubuntu
# Normal user's password
d-i passwd/user-password password ubuntu
d-i passwd/user-password-again password ubuntu
d-i user-setup/encrypt-home boolean false
# The installer will not warn about weak passwords.
d-i user-setup/allow-password-weak boolean true

### Clock and time zone setup

# Set hardware clock to UTC.
d-i clock-setup/utc boolean true
# Europe/Berlin
d-i time/zone select Europe/Berlin
# No NTP during installation
d-i clock-setup/ntp boolean false

### Partitioning

d-i partman-auto/disk string /dev/sda
# Choose LVM
d-i partman-auto/method string lvm
# Remove pre-existing LVM
d-i partman-lvm/device_remove_lvm boolean true
# Remove pre-existing software RAID array
d-i partman-md/device_remove_md boolean true
# Confirm to write the lvm partitions
d-i partman-lvm/confirm boolean true
d-i partman-lvm/confirm_nooverwrite boolean true
# Select the whole disk
d-i partman-auto-lvm/guided_size string max
d-i partman-auto-lvm/new_vg_name string system
d-i partman-partitioning/confirm_write_new_label boolean true
d-i partman/choose_partition select Finish
d-i partman/confirm_nooverwrite boolean true
d-i partman/confirm boolean true
d-i partman-auto/expert_recipe string     \
efi-host-vg ::                            \
  512 512 512 fat32                       \
    $defaultignore{ }                     \
    $reusemethod{ }                       \
    method{ efi }                         \
    format{ }                             \
    .                                     \
  10240 1000 10240 ext4                   \
    $lvmok{ }                             \
    lv_name{ root }                       \
    method{ lvm } format{ }               \
    use_filesystem{ } filesystem{ ext4 }  \
    mountpoint{ / }                       \
    .                                     \
  2048 1000 2048 ext4                     \
    $lvmok{ }                             \
    lv_name{ home }                       \
    method{ lvm } format{ }               \
    use_filesystem{ } filesystem{ ext4 }  \
    mountpoint{ /home }                   \
    .                                     \
  2048 1000 2048 ext4                     \
    $lvmok{ }                             \
    lv_name{ tmp }                        \
    method{ lvm } format{ }               \
    use_filesystem{ } filesystem{ ext4 }  \
    mountpoint{ /tmp }                    \
    .                                     \
  30720 2000 30720 ext4                   \
    $lvmok{ }                             \
    lv_name{ docker }                     \
    method{ lvm } format{ }               \
    use_filesystem{ } filesystem{ ext4 }  \
    mountpoint{ /var/lib/docker }         \
    .                                     \
  1024 2000 1024 ext4                     \
    $lvmok{ }                             \
    lv_name{ audit }                      \
    method{ lvm } format{ }               \
    use_filesystem{ } filesystem{ ext4 }  \
    mountpoint{ /var/log/audit }          \
    .                                     \
  10240 3000 10240 ext4                   \
    $lvmok{ }                             \
    lv_name{ var }                        \
    method{ lvm } format{ }               \
    use_filesystem{ } filesystem{ ext4 }  \
    mountpoint{ /var }                    \
    .                                     \
  8192 3000 8192 ext4                     \
    $lvmok{ }                             \
    lv_name{ swap }                       \
    method{ lvm } format{ }               \
    use_filesystem{ } filesystem{ swap }  \
    .                                     \
  512 5000 8000000000000 ext4             \
    $lvmok{ }                             \
    lv_name{ placeholder }                \
    method{ lvm } format{ }               \
    use_filesystem{ } filesystem{  }      \
    .

### Apt setup

# Repositories
d-i apt-setup/restricted boolean true
d-i apt-setup/universe boolean true
d-i apt-setup/backports boolean true

### Package selection

tasksel tasksel/first multiselect standard, lubuntu-desktop
# Individual additional packages to install
d-i pkgsel/include string openssh-server python htop vim
# No update during installation
d-i pkgsel/upgrade select none
# Language pack selection
d-i pkgsel/language-packs multiselect en
# No language support packages
d-i pkgsel/install-language-support boolean false
# No automatic updates
d-i pkgsel/update-policy select none
# Verbose output and no boot splash screen
d-i debian-installer/quiet  boolean false
d-i debian-installer/splash boolean true

### Boot loader installation

d-i grub-installer/grub2_instead_of_grub_legacy boolean true
d-i grub-installer/only_debian boolean false
d-i grub-installer/with_other_os boolean true
d-i grub-installer/bootdev string default
d-i grub-installer/timeout string 5
# Avoid that last message about the install being complete.
d-i finish-install/reboot_in_progress note