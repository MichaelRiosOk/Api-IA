ALLOWED_DATASETS = {
    "ot_por_estado": """
        SELECT TOP 50 *
        FROM dbo.VW_API_OT_PorEstado_12M
        ORDER BY NU_Anio DESC, NU_Mes DESC
    """,
    "ot_tiempos": """
        SELECT TOP 50 *
        FROM dbo.VW_API_OT_TiemposPromedio_12M
        ORDER BY NU_Anio DESC, NU_Mes DESC
    """,
    "casos_sucursal_familia": """
        SELECT TOP 50 *
        FROM dbo.VW_API_CAS_PorSucursal_Familia_12M
        ORDER BY NU_Anio DESC, NU_Mes DESC
    """
}