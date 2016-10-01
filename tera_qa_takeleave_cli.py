# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tera_qa_takeleave import TeraQATakeLeave

import argparse
import config

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser_subparsers = parser.add_subparsers()

    add = parser_subparsers.add_parser('add')
    add.add_argument('adds', metavar=('name', 'from', 'to'), nargs=3, help='an integer for the accumulator')

    edit = parser_subparsers.add_parser('edit')
    edit.add_argument('edits', nargs=3, help='an integer for the accumulator')

    lists = parser_subparsers.add_parser('list')
    lists.add_argument('lists', nargs=1, help='an integer for the accumulator')

    list_all = parser_subparsers.add_parser('list_all')
    list_all.add_argument('list_all', nargs="*", help='an integer for the accumulator')

    delete = parser_subparsers.add_parser('delete')
    delete.add_argument('deletes', nargs=1, help='an integer for the accumulator')

    args = parser.parse_args()

    takeleave = TeraQATakeLeave(host=config.host, username=config.username, password=config.password, database=config.database)

    if hasattr(args, 'adds'):
        takeleave.insert_data(args.adds[0], args.adds[1], args.adds[2])
    elif hasattr(args, 'edits'):
        takeleave.update_data(args.edits[0], args.edits[1], args.edits[2])
    elif hasattr(args, 'lists'):
        takeleave.list_select_name(args.lists[0])
    elif hasattr(args, 'list_all'):
        takeleave.list_all_data()
    elif hasattr(args, 'deletes'):
        takeleave.delete_data_from_id(args.deletes[0])
