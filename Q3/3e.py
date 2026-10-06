import numpy as np


def project_point(point, width, height, fx, fy, ox, oy, near, far):
    point = np.asarray(point, dtype=float)

    projection = np.array([
        [2 * fx / width, 0, 1 - 2 * ox / width, 0],
        [0, 2 * fy / height, 1 - 2 * oy / height, 0],
        [0, 0, -(far + near) / (far - near), -2 * far * near / (far - near)],
        [0, 0, -1, 0]
    ], dtype=float)

    clip = projection @ point
    ndc = clip[:3] / clip[3]

    pixels = np.array([
        0.5 * (ndc[0] + 1) * width,
        0.5 * (ndc[1] + 1) * height
    ])

    return projection, clip, ndc, pixels


if __name__ == "__main__":
    projection, clip, ndc, pixels = project_point(
        point=(0.3, -0.15, -6.0, 1.0),
        width=800,
        height=600,
        fx=800,
        fy=800,
        ox=400,
        oy=400,
        near=0.2,
        far=20
    )

    print("Projection matrix:\n", projection)
    print("Clip coordinates:", clip)
    print("NDC coordinates:", ndc)
    print("Pixel coordinates:", pixels)
