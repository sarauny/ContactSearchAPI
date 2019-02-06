# search/management/commands/import_company_from_csv.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import csv
from django.core.management.base import BaseCommand
from search.models import Company

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

class Command(BaseCommand):
    help = (
        "Import companies from a local csv file. "
        "Expects id, name, country, and revenue"
    )

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            "file_path",
            nargs=1,
            type=str,
        )

    def handle(self, *args, **options):
        verbosity = options.get("verbosity", NORMAL)
        file_path = options["file_path"][0]

        if verbosity >= NORMAL:
            self.stdout.write("=== Companies imported ===")
        
        with open(file_path) as f: 
            reader = csv.reader(f)
            for rownum, (company_id, name, country, revenue) in \
                enumerate(reader):
                if rownum == 0:
                    # skipping the first column captions
                    continue
                company, created = \
                    Company.objects.get_or_create(
                    id=company_id,
                    name=name,
                    country=country,
                    revenue=revenue,
                )
                if verbosity >= NORMAL:
                    self.stdout.write("{}. {}".format(
                        rownum, company.name
                    ))
