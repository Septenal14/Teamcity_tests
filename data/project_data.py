from utils.custom_faker import DataGenerator
from pydantic import BaseModel
from typing import Optional


class ProjectDataModel(BaseModel):
    parentProject: dict
    name: str
    id: str
    copyAllAssociatedSettings: bool


class ProjectData:
    @staticmethod
    def create_project_data() -> ProjectDataModel:
        return ProjectDataModel(
            parentProject={"locator": "_Root"},
            name=DataGenerator.fake_name(),
            id=DataGenerator.fake_project_id(),
            copyAllAssociatedSettings=True
        )

    @staticmethod
    def create_project_data_negative(project_data):
        return {
            "parentProject": {"locator": "_Root"},
            "name": DataGenerator.fake_name(),
            "id": project_data,
            "copyAllAssociatedSettings": True
        }

    """
    response model -----------------------------------------
    """


class ParentProjectModel(BaseModel):
    id: str
    name: str
    description: str
    href: str
    webUrl: str


class BuildTypeModel(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None


class BuildTypes(BaseModel):
    count: int
    buildType: list[BuildTypeModel] = []


class PropertyModel(BaseModel):
    name: str
    value: str


class Templates(BaseModel):
    count: int
    buildType: list[BuildTypeModel] = []


class ParametersModel(BaseModel):
    property: Optional[list[PropertyModel]] = None
    count: int
    href: str


class ProjectResponseModel(BaseModel):
    id: str
    name: str
    parentProjectId: str
    virtual: bool
    description: Optional[str] = None
    href: str
    webUrl: str
    parentProject: ParentProjectModel
    buildTypes: Optional[BuildTypes] = None
    templates: Optional[Templates] = None
    deploymentDashboards: Optional[dict[str, int]] = None
    parameters: Optional[ParametersModel] = None
    vcsRoots: dict
    projectFeatures: dict
    projects: dict

    class Config:
        extra = "allow"
