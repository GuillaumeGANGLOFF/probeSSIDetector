# Basic-Linux-Privilege-Escalation-Audit

## Description
Based on the read off [[Probing for Password]](https://svs.informatik.uni-hamburg.de/publications/2022/2022-06-08_Probing_for_Passwords.pdf) and on the work of [[xartists/AdminSys]](https://github.com/xartistsAdminsys/flipper/tree/main/probes), this script analyzes for all the SSIDs detected after a sniffing probes.

## Disclaimer
This script is provided for educational purposes only. Use of this script for testing, either on your own systems or on systems for which you have legal authorization to perform such tests, is highly encouraged. However, executing this script on systems without such authorization is illegal and strictly forbidden. The creator of this script assumes no liability for misuse of this tool or any damage that might be caused by its appropriate or inappropriate use. It is the end user's responsibility to comply with all applicable local, state, and federal laws. Users must consider the impact of any actions they perform and be mindful of the applicable laws and rights of others.

By running this script, you agree to the terms of use and acknowledge that you have the necessary authorizations to perform such assessments.

## Usage

You can use it with only probes requests or after a general monitoring.

1. Make the script executable:
    ```bash
    chmod +x main.py
    ```

2. Dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Execute the script:
    ```bash
    ./main.py --pcap [[file_path]] --output [[file_path]] --filter [[int]]
    ```

    --pcap : Path to the PCAP file to analyze.
    --output : Path to the output file for storing results.
    --filter : Optional integer filter for SSID's lenght.

   Exemple:
   ```bash
   ./main.py --pcap probes_1.pcap --output result.txt --filter 8
    
## License
This project is licensed under the MIT License.

## Contributing
If you would like to contribute to this project, please fork the repository and create a pull request with your changes. I welcome improvements and suggestions.

## Contact
For any questions or issues, please open an issue in this repository or contact the maintainer.
