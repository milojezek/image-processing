from dataclasses import dataclass
from services.db import run_db_statement

@dataclass
class ScanMetadata:
    """
    Object representing metadata (such as size, destination in Azure Storage or coordinates of bounding boxes) of a
    single scan.
    """
    id: int
    png_image: str
    file_name: str

    def __init__(self, id, png_image, file_name) -> None: 
        self.id = id
        self.png_image = png_image
        self.file_name = file_name


def get_scans_metadata_with_double_match(annotation: str) -> list[ScanMetadata]:
    """
    Query the database for all scans that have a double label match (2 different annotators agree on some label).
    You can choose one of theses annotations:
    - benign_microcalsifications
    - malign_microcalsifications
    - malign_mass
    - benign_mass
    """

    # SQL query that will select all items from scans whose id is equal to scan id in an annotation 
    # whose has_{annotation} is TRUE and whose study id is at least twice in the scan table.
    query = f"""
    SELECT scan.id, scan.png_image, scan.file_name
    FROM mmgscans_mmgscan scan
    JOIN mmgscans_mmgscanannotation annotation ON scan.id = annotation.mmg_scan_id
    WHERE annotation.has_{annotation} = TRUE
    AND scan.mmg_study_id IN (
        SELECT mmg_study_id
        FROM mmgscans_mmgscan
        GROUP BY mmg_study_id
        HAVING COUNT(*) >= 2
    );
    """

    scan_result = run_db_statement(query)
    scans_metadata = list(map(lambda result: ScanMetadata(result[0], result[1], result[2]), scan_result))

    return scans_metadata


def download_scan_png(scan_metadata: ScanMetadata) -> None:
    """
    Download the scan (in PNG format) from Azure Storage and save it to the local filesystem.
    Destination directory where the files will be saved is defined by the `PNG_DIR` environment variable.

    Hint: Use the `get_blob_as_bytes` function from the `services.azure_storage` module.
    """
    


def draw_bounding_boxes(annotation: str, scan_metadata: ScanMetadata) -> None:
    """
    Load PNG file from the local filesystem, draw bounding boxes (defined in `scan_metadat` metadata) on it and save it
    back to the local filesystem.
    PNG file is loaded from the directory defined by the `PNG_DIR` environment variable.
    Destination directory where the files will be saved is defined by the `BBOXES_DIR` environment variable.
    """
    raise NotImplementedError()


def main(annotation: str) -> None:
    scans_metadata = get_scans_metadata_with_double_match(annotation)
    
    for metadata in scans_metadata:
        print(metadata)

    # for scan_metadata in scans_metadata:
    #     download_scan_png(scan_metadata)
    #     draw_bounding_boxes(annotation, scan_metadata)