endpoints = {
  'get_best_practices': {
    'path': '/best_practice.json/get_best_practices',
    'params': ['date', 'aws_accounts_ids'],
  },
  'get_changes': {
    'path': '/change_monitoring.json/get_changes',
    'params': ['start', 'end', 'resource_id'],
  },
  'get_detailed_billing_analysis': {
    'path': '/billing.json/get_detailed_billing_analysis',
    'params': ['saved_filter_name', 'start', 'end'],
  },
  'get_detailed_billing_analysis_with_grouping': {
    'path': '/billing.json/get_detailed_billing_with_grouping',
    'params': ['saved_filter_name', 'start', 'end'],
  },
  'add_account': {
    'path': '/account.json/add_account',
    'params': ['account_name', 'user_name'],
  },
  'delete_account': {
    'path': '/account.json/delete_account',
    'params': ['account_name'],
  },
  'tag_account': {
    'path': '/account.json/tag_account',
    'params': ['account_name', 'account_tag'],
  },
  'untag_account': {
    'path': '/account.json/untag_account',
    'params': ['account_name', 'account_tag'],
  },
  'get_history': {
    'path': '/CloudWatch.json/get_history',
    'params': ['service', 'start', 'end'],
  },
  'get_resources': {
    'path': '/inventory.json/get_resources',
    'params': ['date']
  },
  'get_resources_ec2_summary': {
    'path': '/inventory.json/get_resources_ec2_summary',
    'params': ['date']
  },
  'get_resources_ec2_details': {
    'path': '/inventory.json/get_resources_ec2_details',
    'params': ['date', 'aws_accounts_ids', 'instance_ids', 'resource_tags']
  },
  'get_resources_s3_summary': {
    'path': '/inventory.json/get_resources_s3_summary',
    'params': ['date']
  },
  'get_resources_s3_details': {
    'path': '/inventory.json/get_resources_s3_details',
    'params': ['date', 'bucket_names', 'aws_accounts_ids']
  },
  'get_resources_rds_summary': {
    'path': '/inventory.json/get_resources_rds_summary',
    'params': ['date']
  },
  'get_resources_rds_details': {
    'path': '/inventory.json/get_resources_rds_details',
    'params': ['date', 'instance_ids', 'resource_tags', 'aws_accounts_ids']
  },
  'get_resources_ebs_summary': {
    'path': '/inventory.json/get_resources_ebs_summary',
    'params': ['date']
  },
  'get_resources_ebs_details': {
    'path': '/inventory.json/get_resources_ebs_details',
    'params': ['date', 'volume_ids', 'resource_tags', 'aws_accounts_ids']
  },
  'get_resources_ebs_snapshots': {
    'path': '/inventory.json/get_resources_ebs_snapshots',
    'params': ['date', 'snapshot_ids', 'volume_ids']
  },
  'get_resources_ami_summary': {
    'path': '/inventory.json/get_resources_ami_summary',
    'params': ['date']
  },
  'get_resources_ami_details': {
    'path': '/inventory.json/get_resources_ami_details',
    'params': ['date', 'names', 'aws_accounts_ids']
  },
  'ec2_security_group_summary': {
    'path': '/inventory.json/ec2_security_group_summary',
    'params': ['date']
  },
  'ec2_security_group_details': {
    'path': '/inventory.json/ec2_security_group_details',
    'params': ['date', 'group_ids', 'security_groups', 'vpc_ids',
               'aws_accounts_ids']
  },
}

for endpoint in endpoints:
  endpoints[endpoint]['method'] = 'GET'
  endpoints[endpoint]['status'] = 200
