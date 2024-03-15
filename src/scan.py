from dataclasses import dataclass


@dataclass
class ScanMetadata:
    """
    Object representing metadata (such as size, destination in Azure Storage or coordinates of bounding boxes) of a
    single scan.
    """


def get_scans_metadata_with_double_match(annotation: str) -> list[ScanMetadata]:
    """
    Query the database for all scans that have a double label match (2 different annotators agree on some label).

    Hint: You can use the `run_db_statement` function from the `services.db` module to execute the SQL query.
    """
    raise NotImplementedError()


def download_scan_png(scan_metadata: ScanMetadata) -> None:
    """
    Download the scan (in PNG format) from Azure Storage and save it to the local filesystem.
    Destination directory where the files will be saved is defined by the `PNG_DIR` environment variable.

    Hint: Use the `get_blob_as_bytes` function from the `services.azure_storage` module.
    """
    raise NotImplementedError()


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

    for scan_metadata in scans_metadata:
        download_scan_png(scan_metadata)
        draw_bounding_boxes(annotation, scan_metadata)
