# search/management/commands/import_contact_from_csv.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import csv
from django.core.management.base import BaseCommand
from search.models import Contact, Company

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

class Command(BaseCommand):
    help = (
        "Import Contacts from a local csv file. "
        "Expects id, name, emal, and company_id"
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
            self.stdout.write("=== Contacts imported ===")
        
        with open(file_path) as f: 
            reader = csv.reader(f)
            for rownum, (contactid, name, email, company_id) in \
                enumerate(reader):
                if rownum == 0:
                    # skipping the first column captions
                    continue
                contact, created = \
                    Contact.objects.get_or_create(
                    id=contactid,
                    name=name,
                    email=email,
                    company_id=company_id,
                )
                if verbosity >= NORMAL:
                    self.stdout.write("{}. {}".format(
                        rownum, contact.email
                    ))

