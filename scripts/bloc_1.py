import os
import json
from datetime import datetime, timedelta
from pathlib import Path

class ReportGenerator:
    """Genera informes d'incidències per dia, setmana o mes."""
    
    def __init__(self, incidents_dir: str = "data/incidents"):
        self.incidents_dir = Path(incidents_dir)
        
    def load_incidents(self) -> list:
        """Carrega totes les incidències dels fitxers YAML."""
        incidents = []
        if not self.incidents_dir.exists():
            return incidents
            
        for filepath in self.incidents_dir.glob("*.yaml"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    import yaml
                    incident = yaml.safe_load(f)
                    if incident:
                        incidents.append(incident)
            except Exception:
                continue
        return incidents
    
    def generate_daily_report(self, date: str) -> dict:
        """Genera informe diari per una data concreta (format YYYY-MM-DD)."""
        incidents = self.load_incidents()
        filtered = [i for i in incidents if i.get("data_creacio", "").startswith(date)]
        
        total = len(filtered)
        resoltes = len([i for i in filtered if i.get("estat") == "resolta"])
        tancades = len([i for i in filtered if i.get("estat") == "tancada"])
        actives = len([i for i in filtered if i.get("estat") in ("oberta", "en curs")])
        
        per_prioritat = {}
        per_categoria = {}
        per_estat = {}
        
        for inc in filtered:
            p = inc.get("prioritat", "desconeguda")
            per_prioritat[p] = per_prioritat.get(p, 0) + 1
            
            c = inc.get("categoria", "sense")
            per_categoria[c] = per_categoria.get(c, 0) + 1
            
            e = inc.get("estat", "desconegut")
            per_estat[e] = per_estat.get(e, 0) + 1
        
        temps_resolucio = []
        for inc in filtered:
            if inc.get("data_resolucio") and inc.get("data_creacio"):
                try:
                    t1 = datetime.fromisoformat(inc["data_creacio"].replace("Z", "+00:00"))
                    t2 = datetime.fromisoformat(inc["data_resolucio"].replace("Z", "+00:00"))
                    diff = (t2 - t1).total_seconds() / 3600
                    temps_resolucio.append(diff)
                except:
                    pass
        
        temps_mig = sum(temps_resolucio) / len(temps_resolucio) if temps_resolucio else 0
        
        return {
            "tipus": "diari",
            "data": date,
            "metriques": {
                "total_creades": total,
                "total_resoltes": resoltes,
                "total_tancades": tancades,
                "actives": actives,
                "per_prioritat": per_prioritat,
                "per_categoria": per_categoria,
                "per_estat": per_estat,
                "temps_mig_resolucio_hores": round(temps_mig, 2)
            },
            "incidencies": [i.get("id") for i in filtered]
        }
    
    def generate_weekly_report(self, year: int, week: int) -> dict:
        """Genera informe setmanal."""
        incidents = self.load_incidents()
        start = datetime.strptime(f"{year}-W{week:02d}-1", "%Y-W%W-%w")
        end = start + timedelta(days=7)
        
        filtered = []
        for inc in incidents:
            try:
                d = datetime.fromisoformat(inc.get("data_creacio", "").replace("Z", "+00:00"))
                if start <= d < end:
                    filtered.append(inc)
            except:
                continue
        
        total = len(filtered)
        resoltes = len([i for i in filtered if i.get("estat") == "resolta"])
        tancades = len([i for i in filtered if i.get("estat") == "tancada"])
        actives = len([i for i in filtered if i.get("estat") in ("oberta", "en curs")])
        
        per_prioritat = {}
        per_estat = {}
        per_categoria = {}
        per_proveidor = {}
        
        for inc in filtered:
            p = inc.get("prioritat", "desconeguda")
            per_prioritat[p] = per_prioritat.get(p, 0) + 1
            e = inc.get("estat", "desconegut")
            per_estat[e] = per_estat.get(e, 0) + 1
            c = inc.get("categoria", "sense")
            per_categoria[c] = per_categoria.get(c, 0) + 1
            prov = inc.get("proveidor_assignat", "sense")
            per_proveidor[prov] = per_proveidor.get(prov, 0) + 1
        
        temps_resolucio = []
        for inc in filtered:
            if inc.get("data_resolucio") and inc.get("data_creacio"):
                try:
                    t1 = datetime.fromisoformat(inc["data_creacio"].replace("Z", "+00:00"))
                    t2 = datetime.fromisoformat(inc["data_resolucio"].replace("Z", "+00:00"))
                    diff = (t2 - t1).total_seconds() / 3600
                    temps_resolucio.append(diff)
                except:
                    pass
        
        temps_mig = sum(temps_resolucio) / len(temps_resolucio) if temps_resolucio else 0
        mitjana_creades = round(total / 7, 2) if total > 0 else 0
        mitjana_resoltes = round(resoltes / 7, 2) if resoltes > 0 else 0
        
        # Tendència
        meitat = len(filtered) // 2
        primera_meitat = len([i for i in filtered[:meitat]])
        segona_meitat = len([i for i in filtered[meitat:]])
        if segona_meitat > primera_meitat * 1.1:
            tendencia = "creixent"
        elif segona_meitat < primera_meitat * 0.9:
            tendencia = "decreixent"
        else:
            tendencia = "estable"
        
        top_categories = sorted(per_categoria.items(), key=lambda x: x[1], reverse=True)[:3]
        top_proveidors = sorted(per_proveidor.items(), key=lambda x: x[1], reverse=True)[:3]
        
        return {
            "tipus": "setmanal",
            "setmana": week,
            "any": year,
            "data_inici": start.strftime("%Y-%m-%d"),
            "data_fi": (end - timedelta(days=1)).strftime("%Y-%m-%d"),
            "metriques": {
                "total_creades": total,
                "total_resoltes": resoltes,
                "total_tancades": tancades,
                "actives": actives,
                "mitjana_creades_per_dia": mitjana_creades,
                "mitjana_resoltes_per_dia": mitjana_resoltes,
                "tendencia": tendencia,
                "critiques_no_resoltes": len([i for i in filtered if i.get("prioritat") == 1 and i.get("estat") in ("oberta", "en curs")]),
                "top_categories": [{"categoria": k, "total": v} for k, v in top_categories],
                "top_proveidors": [{"proveidor": k, "total": v} for k, v in top_proveidors],
                "per_prioritat": per_prioritat,
                "per_estat": per_estat,
                "temps_mig_resolucio_hores": round(temps_mig, 2)
            },
            "incidencies": [i.get("id") for i in filtered]
        }
    
    def generate_monthly_report(self, year: int, month: int) -> dict:
        """Genera informe mensual."""
        incidents = self.load_incidents()
        filtered = []
        for inc in incidents:
            try:
                d = datetime.fromisoformat(inc.get("data_creacio", "").replace("Z", "+00:00"))
                if d.year == year and d.month == month:
                    filtered.append(inc)
            except:
                continue
        
        total = len(filtered)
        resoltes = len([i for i in filtered if i.get("estat") == "resolta"])
        tancades = len([i for i in filtered if i.get("estat") == "tancada"])
        actives = len([i for i in filtered if i.get("estat") in ("oberta", "en curs")])
        
        per_prioritat = {}
        per_estat = {}
        per_categoria = {}
        per_proveidor = {}
        evolucio_diaria = {}
        
        for inc in filtered:
            p = inc.get("prioritat", "desconeguda")
            per_prioritat[p] = per_prioritat.get(p, 0) + 1
            e = inc.get("estat", "desconegut")
            per_estat[e] = per_estat.get(e, 0) + 1
            c = inc.get("categoria", "sense")
            per_categoria[c] = per_categoria.get(c, 0) + 1
            prov = inc.get("proveidor_assignat", "sense")
            per_proveidor[prov] = per_proveidor.get(prov, 0) + 1
            
            dia = inc.get("data_creacio", "")[:10]
            evolucio_diaria[dia] = evolucio_diaria.get(dia, 0) + 1
        
        temps_resolucio = []
        temps_per_categoria = {}
        for inc in filtered:
            if inc.get("data_resolucio") and inc.get("data_creacio"):
                try:
                    t1 = datetime.fromisoformat(inc["data_creacio"].replace("Z", "+00:00"))
                    t2 = datetime.fromisoformat(inc["data_resolucio"].replace("Z", "+00:00"))
                    diff = (t2 - t1).total_seconds() / 3600
                    temps_resolucio.append(diff)
                    cat = inc.get("categoria", "altre")
                    if cat not in temps_per_categoria:
                        temps_per_categoria[cat] = []
                    temps_per_categoria[cat].append(diff)
                except:
                    pass
        
        temps_mig = sum(temps_resolucio) / len(temps_resolucio) if temps_resolucio else 0
        temps_mig_per_categoria = {}
        for cat, temps in temps_per_categoria.items():
            temps_mig_per_categoria[cat] = round(sum(temps) / len(temps), 2)
        
        dies_mes_incidencies = sorted(evolucio_diaria.items(), key=lambda x: x[1], reverse=True)[:5]
        
        start = datetime(year, month, 1)
        if month == 12:
            end = datetime(year + 1, 1, 1)
        else:
            end = datetime(year, month + 1, 1)
        dies_del_mes = (end - start).days
        
        mitjana_creades = round(total / dies_del_mes, 2) if total > 0 else 0
        mitjana_resoltes = round(resoltes / dies_del_mes, 2) if resoltes > 0 else 0
        
        top_categories = sorted(per_categoria.items(), key=lambda x: x[1], reverse=True)[:3]
        top_proveidors = sorted(per_proveidor.items(), key=lambda x: x[1], reverse=True)[:3]
        
        return {
            "tipus": "mensual",
            "mes": month,
            "any": year,
            "data_inici": start.strftime("%Y-%m-%d"),
            "data_fi": (end - timedelta(days=1)).strftime("%Y-%m-%d"),
            "metriques": {
                "total_creades": total,
                "total_resoltes": resoltes,
                "total_tancades": tancades,
                "actives": actives,
                "mitjana_creades_per_dia": mitjana_creades,
                "mitjana_resoltes_per_dia": mitjana_resoltes,
                "tendencia": "estable",
                "critiques_no_resoltes": len([i for i in filtered if i.get("prioritat") == 1 and i.get("estat") in ("oberta", "en curs")]),
                "top_categories": [{"categoria": k, "total": v} for k, v in top_categories],
                "top_proveidors": [{"proveidor": k, "total": v} for k, v in top_proveidors],
                "per_prioritat": per_prioritat,
                "per_estat": per_estat,
                "temps_mig_resolucio_hores": round(temps_mig, 2),
                "temps_mig_per_categoria": temps_mig_per_categoria,
                "evolucio_diaria": evolucio_diaria,
                "dies_mes_incidencies": [{"data": k, "total": v} for k, v in dies_mes_incidencies]
            },
            "incidencies": [i.get("id") for i in filtered]
        }


if __name__ == "__main__":
    generator = ReportGenerator()
    
    # Exemple d'ús
    print("=== INFORME DIARI ===")
    daily = generator.generate_daily_report("2026-07-16")
    print(json.dumps(daily, indent=2, ensure_ascii=False))
    
    print("\n=== INFORME SETMANAL ===")
    weekly = generator.generate_weekly_report(2026, 29)
    print(json.dumps(weekly, indent=2, ensure_ascii=False))
    
    print("\n=== INFORME MENSUAL ===")
    monthly = generator.generate_monthly_report(2026, 7)
    print(json.dumps(monthly, indent=2, ensure_ascii=False))