#!/usr/bin/env python3

import argparse
from scapy.all import PcapReader
from scapy.layers.dot11 import Dot11Elt, Dot11ProbeReq
import os


def main():
    list_unique_ssid = []
    parser = argparse.ArgumentParser(description='Detects unique SSIDs from a given PCAP file and saves them to an output file.')
    parser.add_argument('--pcap', type=str, required=True, help='Path to the input PCAP file')
    parser.add_argument('--output', type=str, required=True, help='Path to the output file where unique SSIDs will be saved')
    parser.add_argument('--filter', type=int, required=False, default=0, help='Filter out SSIDs with less than the specified number of occurrences')
    args = parser.parse_args()

    output_file = args.output
    pcap_file = args.pcap
    filter_number = args.filter

    print(pcap_file)
    print(output_file)
    print(filter_number)

    if not os.path.isfile(pcap_file):
        print(f"Error: The file {pcap_file} does not exist.")
        return
    
    if os.path.isfile(output_file):
        print(f"The file {output_file} already exists.")
        print("Do you want to overwrite it? press y/yes to continue, any key to exit.")
        answer = input()
        if answer != 'y' or answer != 'yes':
            print("Bye!")
            return
        
    probes = PcapReader(pcap_file)
    print("Searching for unique SSIDs...")
    for probe in probes:
        if probe.haslayer(Dot11ProbeReq):
            ssid = probe[Dot11Elt].info.decode()
            if ssid not in list_unique_ssid and ssid != '' and len(ssid)>=filter_number:
                list_unique_ssid.append(ssid)
    
    try:
        with open(output_file, 'w') as f:
            for ssid in list_unique_ssid:
                f.write(ssid + '\n')
        print(f"Saved successfully: {len(list_unique_ssid)} unique SSIDs found.")
    except Exception as e:
        print(f"Error while saving: {e}")

if __name__=='__main__':
    main()
