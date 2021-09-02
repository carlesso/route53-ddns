#!/usr/bin/env python3

from route53_ddns.route53_interface import update_record
from route53_ddns.ip_utilities import get_ip, verify_propagation, wait_for_propagation
import click

import sys
import logging


def _setup_logging(verbose: bool = False):
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[handler])



@click.command()
@click.option("--zone", required=True, type=str)
@click.option("--record", required=True, type=str)
@click.option("-c", "--check-only", is_flag=True, default=False)
@click.option("-d", "--dryrun", is_flag=True, default=False)
@click.option("-v", "--verbose", is_flag=True, default=False)
def route53_ddns(zone: str, record: str, check_only: bool, dryrun: bool, verbose: bool):
    _setup_logging(verbose=verbose)
    if not record.endswith(zone):
        record = f"{record}.{zone}"
        logging.info(f"Adjusting target record to be {record}")

    target_ip = get_ip()

    if check_only:
        verify_propagation(record=record, target_ip=target_ip)
        return

    update_record(zone_name=zone, record_name=record, target_ip=target_ip, dryrun=dryrun)
    wait_for_propagation(record=record, target_ip=target_ip)


if __name__ == '__main__':
    route53_ddns()
