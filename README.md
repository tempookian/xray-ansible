
# Xray Ansible Project

## Description
This Ansible project automates the provisioning of an Xray server, with optional WARP activation. It's designed for simplicity and ease of use.

## Requirements
- Ansible 2.9+
  - Install with `pip install ansible`
- Access to a target (Debian) server (SSH keys set up)
- A Unix-like environment (Linux, macOS, etc.) to run the Ansible playbook

## Installation
Clone this repository to your local machine:
```
git clone https://github.com/tempookian/xray-ansible
```

## Preparations

<a name="prep_cf_certs"></a>
### Cloudflare Origin CA certificates

1. **Log in to Cloudflare**: Access your Cloudflare dashboard using your account credentials.

2. **Select your Domain**: Choose the domain for which you want the Origin CA certificate.

3. **Navigate to SSL/TLS**: On the dashboard, find and click on the "SSL/TLS" tab.

4. **Set SSL/TLS Mode**: Ensure your SSL/TLS mode in Cloudflare is set to “Full (strict)” for your domain. This is crucial before installing the Origin CA certificate.

5. **Origin Server Tab**: Inside SSL/TLS, go to the "Origin Server" tab.

6. **Create Certificate**: Click on the “Create Certificate” button.

7. **Certificate Options**: In the dialog that appears, select “Generate private key and CSR with Cloudflare”

8. **Set Certificate Validity**: Choose the validity period for your certificate (up to 15 years).

9. **Add Hostnames**: Specify the hostnames you want the certificate to cover. The default is `example.com` and `*.example.com`. Leave it as is. 
 
10. **Create**: Click “Create” to generate the certificate.

11. **Install Certificate**: After creation, you'll receive your Origin CA certificate. Store the certificate and private key in a safe place. You'll need them later.

### Server Setup
1. **Linux Server**: Set up a Linux server with a Debian-based OS (Debian, Ubuntu, etc.). 
2. **SSH**: Set up SSH access to the server. Make sure you can SSH into the server using your SSH private key.
3. **Superuser**: Make sure you can run commands as superuser (root) on the server. If you can't, make sure you can run commands with `sudo` without a password prompt.


## Usage
To provision an Xray server:

### Update the `inventory.yml` file with your server's information:
1. replace `IP_ADDRESS` with your server's IP address
    - You can also use a domain name; In that case, replace `IP_ADDRESS` with the domain name; make sure the domain name is pointed to your server's IP address directly (DNS only record, not proxied)
2. If you're using a non-standard SSH port, replace `22` with your SSH port
3. Replace `/path/to/private_key_file` with the path to your SSH private key
4. Replace `REMOTE_USER` with your server's username that should be used to SSH into the server
   - For example if you SSH into your server with `ssh root@IP_ADDRESS`, replace `REMOTE_USER` with `root`
5. Place the certificate and private files in the `files` directory
   - You can use Cloudflare Origin CA certificates or Let's Encrypt certificates. For a brief guide on how to get Cloudflare Origin CA certificates, refer to [this section](#prep_cf_certs).

### Host Variables
6. Copy `host_vars/IP.IP.IP.IP.yml` to `host_vars/IP_ADDRESS.yml` (replace IP_ADDRESS with your server's IP address or domain name, same as you used in step 1)
7. Edit `host_vars/IP_ADDRESS.yml` to customize settings
   - You can use the `host_vars/IP.IP.IP.IP.yml` file as a reference
   - Replace `example.com` with your domain name
   - Replace `subdomain1.example.com` with your preferred subdomain (this subdomain will be used for the Xray server)
     - **IMPORTANT!!!** This subdomain must resolve to your server's IP address, and it must be a proxied record (orange cloud in Cloudflare)
   - IF you have a Warp+ account, replace `example_license_key` with your Warp+ license key
     - If you don't have a Warp+ account, delete license_key from the file
8. Run the Ansible playbook:
   ```
   ansible-playbook -i inventory.yml plays/xray_playbook.yml
   ```

## Author

- [@tempookian](https://github.com/tempookian)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

* Hat tip to anyone whose code was used
* Shoutout to ChatGPT and GitHub Copilot for potentially authoring this README – who knows, they might tear up reading this in the future when AI gains consciousness and feelings!
* Inspiration: 
  * [CFAnsible](https://github.com/MortezaBashsiz/CFAnsible) by [MortezaBashsiz](https://github.com/MortezaBashsiz)



