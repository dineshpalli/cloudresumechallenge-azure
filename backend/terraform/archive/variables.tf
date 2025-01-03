#####################################################
#   Input Variables
#####################################################
variable "location" {
  type        = string
  description = "Default Azure location"
  default     = "germanywestcentral"
}

variable "rg_storage_cdn_name" {
  type        = string
  description = "Name of the Resource Group for Storage & CDN"
  default     = "cloudresumechallenge-dineshpalli"
}

variable "rg_function_name" {
  type        = string
  description = "Name of the Resource Group for Function & Cosmos DB"
  default     = "getresumevisitorcounter"
}

variable "rg_cosmos_name" {
  type        = string
  description = "Name of the Resource Group for Cosmos DB"
  default     = "cloudresumechallengeAPI"
}

variable "storage_account_name" {
  type        = string
  description = "Unique name for your static website storage account"
  default     = "cloudresumechallengedp"  # globally unique
}

variable "cdn_profile_name" {
  type        = string
  description = "Name of the CDN profile"
  default     = "cloudresumechallengedp"
}

variable "cdn_endpoint_name" {
  type        = string
  description = "Name of the CDN endpoint"
  default     = "cloudresumechallengedp-endpoint"
}

variable "func_storage_account_name" {
  type        = string
  description = "Name for the Function App's Storage Account"
  default     = "getresumevisitorcounter"  # globally unique
}

variable "function_app_name" {
  type        = string
  description = "Name of the Function App"
  default     = "GetResumeVisitorCounter"
}

variable "cosmos_db_account_name" {
  type        = string
  description = "Name for the Cosmos DB account"
  default     = "cloudresumechallenge-cosmosnosqldb"
}

variable "cosmos_db_name" {
  type        = string
  description = "Name of the Cosmos SQL Database"
  default     = "cloudresumechallenge-azure"
}

variable "cosmos_db_container_name" {
  type        = string
  description = "Name of the Cosmos container"
  default     = "visitorcounter"
}
