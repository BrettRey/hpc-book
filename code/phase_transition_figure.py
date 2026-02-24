"""
Generate a three-panel phase transition figure (Ice Ih → Liquid Water → Steam)
with chemically accurate ice Ih structure and consistent visual style.

All three panels use the same H₂O molecule representation:
  - Large blue sphere = oxygen
  - Two small white/light-blue spheres = hydrogen (at ~104.5° bond angle)
  - Dashed lines = hydrogen bonds

Ice panel: tetrahedral coordination, puckered hexagonal rings (c-axis view).
Liquid panel: disordered clusters with transient H-bonds.
Steam panel: isolated molecules, widely spaced.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

np.random.seed(42)

# ── Style constants ───────────────────────────────────────────────

O_COLOR = '#4A90D9'
O_EDGE = '#2C5F8A'
H_COLOR = '#D0E4F7'
H_EDGE = '#8AB4D8'
BOND_COLOR = '#5A9BD4'
HBOND_COLOR = '#A0C4E8'
BG_COLOR = '#F5F3EF'


# ── Molecule drawing ──────────────────────────────────────────────

def draw_molecule(ax, x, y, angle_deg=0, scale=1.0, alpha=1.0):
    """Draw a single H₂O molecule at (x,y) with orientation angle_deg.

    Returns: (o_pos, h1_pos, h2_pos) as (x,y) tuples.
    """
    o_r = 0.16 * scale
    h_r = 0.085 * scale
    bond_len = 0.28 * scale
    bond_angle = 104.5
    half = bond_angle / 2

    a1 = np.radians(angle_deg + half)
    a2 = np.radians(angle_deg - half)
    h1x, h1y = x + bond_len * np.cos(a1), y + bond_len * np.sin(a1)
    h2x, h2y = x + bond_len * np.cos(a2), y + bond_len * np.sin(a2)

    # Covalent bonds
    lw = 2.2 * scale
    ax.plot([x, h1x], [y, h1y], color=BOND_COLOR, lw=lw, alpha=alpha,
            zorder=1, solid_capstyle='round')
    ax.plot([x, h2x], [y, h2y], color=BOND_COLOR, lw=lw, alpha=alpha,
            zorder=1, solid_capstyle='round')

    # Oxygen (draw with slight gradient effect via layered circles)
    ax.add_patch(plt.Circle((x, y), o_r, fc=O_COLOR, ec=O_EDGE,
                            lw=0.7*scale, alpha=alpha, zorder=3))
    # Highlight
    ax.add_patch(plt.Circle((x - o_r*0.25, y + o_r*0.25), o_r*0.35,
                            fc='white', ec='none', alpha=0.25*alpha, zorder=4))

    # Hydrogens
    for hx, hy in [(h1x, h1y), (h2x, h2y)]:
        ax.add_patch(plt.Circle((hx, hy), h_r, fc=H_COLOR, ec=H_EDGE,
                                lw=0.5*scale, alpha=alpha, zorder=2))
        ax.add_patch(plt.Circle((hx - h_r*0.2, hy + h_r*0.2), h_r*0.3,
                                fc='white', ec='none', alpha=0.2*alpha, zorder=4))

    return (x, y), (h1x, h1y), (h2x, h2y)


def draw_hbond(ax, x1, y1, x2, y2, alpha=0.45):
    """Draw a hydrogen bond (dashed line)."""
    ax.plot([x1, x2], [y1, y2], color=HBOND_COLOR, lw=1.2, ls=(0, (4, 3)),
            alpha=alpha, zorder=0)


# ── Ice Ih panel ──────────────────────────────────────────────────

def make_ice_panel(ax):
    """
    Ice Ih viewed along the c-axis. Puckered hexagonal rings are shown
    by alternating two molecule sizes (front layer = larger, back = smaller/fainter).
    Molecules are oriented so that one H points toward a neighbour's O,
    showing directional hydrogen bonding.
    """
    # Build hex lattice: vertices of tessellating hexagons
    hex_r = 0.62  # ring radius
    mol_dict = {}  # key -> (x, y, layer)

    # Generate hexagonal ring centres
    ring_centres = []
    for row in range(5):
        for col in range(4):
            cx = col * hex_r * np.sqrt(3)
            cy = row * hex_r * 1.5
            if row % 2 == 1:
                cx += hex_r * np.sqrt(3) / 2
            ring_centres.append((cx, cy))

    # Place molecules at hex vertices, snapping shared vertices
    for cx, cy in ring_centres:
        for v in range(6):
            ang = np.radians(60 * v + 30)
            mx = cx + hex_r * np.cos(ang)
            my = cy + hex_r * np.sin(ang)
            key = (round(mx, 1), round(my, 1))
            if key not in mol_dict:
                layer = v % 2  # alternate puckering
                mol_dict[key] = (mx, my, layer)

    # Sort: draw back layer first, then front
    back = [(k, v) for k, v in mol_dict.items() if v[2] == 1]
    front = [(k, v) for k, v in mol_dict.items() if v[2] == 0]

    # Draw H-bonds first (behind everything)
    all_pos = list(mol_dict.values())
    for i in range(len(all_pos)):
        for j in range(i+1, len(all_pos)):
            x1, y1, _ = all_pos[i]
            x2, y2, _ = all_pos[j]
            d = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            if 0.4 < d < 0.85:
                draw_hbond(ax, x1, y1, x2, y2, alpha=0.35)

    # Draw molecules: back layer (smaller, fainter) then front (full size)
    for _, (mx, my, layer) in back:
        # Orient toward nearest neighbour (crude but gives directional look)
        neighbours = [(v[0]-mx, v[1]-my) for v in all_pos
                      if 0.3 < np.sqrt((v[0]-mx)**2+(v[1]-my)**2) < 0.85]
        if neighbours:
            dx, dy = neighbours[0]
            orient = np.degrees(np.arctan2(dy, dx))
        else:
            orient = np.random.uniform(0, 360)
        draw_molecule(ax, mx, my, orient, scale=0.75, alpha=0.55)

    for _, (mx, my, layer) in front:
        neighbours = [(v[0]-mx, v[1]-my) for v in all_pos
                      if 0.3 < np.sqrt((v[0]-mx)**2+(v[1]-my)**2) < 0.85]
        if neighbours:
            dx, dy = neighbours[0]
            orient = np.degrees(np.arctan2(dy, dx))
        else:
            orient = np.random.uniform(0, 360)
        draw_molecule(ax, mx, my, orient, scale=1.0, alpha=1.0)

    ax.set_xlim(-0.4, 4.6)
    ax.set_ylim(-0.4, 5.0)
    ax.set_aspect('equal')
    ax.set_title('Ice', fontsize=12, fontweight='bold', pad=10,
                 fontfamily='sans-serif')
    ax.text(0.5, -0.06, 'Ice Ih', transform=ax.transAxes, ha='center',
            fontsize=9, fontstyle='italic', fontfamily='sans-serif')


# ── Liquid water panel ────────────────────────────────────────────

def make_liquid_panel(ax):
    """Liquid water: disordered but clustered, with transient H-bonds."""
    n = 28
    positions = []
    for _ in range(n * 10):  # attempts
        x = np.random.uniform(0.4, 4.4)
        y = np.random.uniform(0.4, 4.8)
        ok = all(np.sqrt((x-px)**2 + (y-py)**2) > 0.58 for px, py in positions)
        if ok:
            positions.append((x, y))
        if len(positions) >= n:
            break

    for x, y in positions:
        orient = np.random.uniform(0, 360)
        draw_molecule(ax, x, y, orient)

    # Transient H-bonds (fewer than ice, some broken)
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            d = np.sqrt((positions[j][0]-positions[i][0])**2 +
                        (positions[j][1]-positions[i][1])**2)
            if 0.58 < d < 0.95 and np.random.random() < 0.45:
                draw_hbond(ax, positions[i][0], positions[i][1],
                          positions[j][0], positions[j][1], alpha=0.25)

    ax.set_xlim(-0.2, 5.0)
    ax.set_ylim(-0.2, 5.2)
    ax.set_aspect('equal')
    ax.set_title('Liquid Water', fontsize=12, fontweight='bold', pad=10,
                 fontfamily='sans-serif')
    ax.text(0.5, -0.06, 'Liquid Water', transform=ax.transAxes, ha='center',
            fontsize=9, fontstyle='italic', fontfamily='sans-serif')


# ── Steam panel ───────────────────────────────────────────────────

def make_steam_panel(ax):
    """Steam: isolated molecules, widely spaced, no H-bonds."""
    n = 10
    positions = []
    for _ in range(n * 20):
        x = np.random.uniform(0.5, 4.3)
        y = np.random.uniform(0.5, 4.8)
        ok = all(np.sqrt((x-px)**2 + (y-py)**2) > 1.2 for px, py in positions)
        if ok:
            positions.append((x, y))
        if len(positions) >= n:
            break

    for x, y in positions:
        orient = np.random.uniform(0, 360)
        draw_molecule(ax, x, y, orient)

    ax.set_xlim(-0.2, 5.0)
    ax.set_ylim(-0.2, 5.2)
    ax.set_aspect('equal')
    ax.set_title('Steam', fontsize=12, fontweight='bold', pad=10,
                 fontfamily='sans-serif')
    ax.text(0.5, -0.06, 'Steam', transform=ax.transAxes, ha='center',
            fontsize=9, fontstyle='italic', fontfamily='sans-serif')


# ── Composite figure ──────────────────────────────────────────────

fig, axes = plt.subplots(1, 3, figsize=(14, 7.65))  # ~1.83:1

for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_facecolor(BG_COLOR)

fig.patch.set_facecolor(BG_COLOR)

make_ice_panel(axes[0])
make_liquid_panel(axes[1])
make_steam_panel(axes[2])

# Vertical dividers
for i in [1, 2]:
    x = (axes[i-1].get_position().x1 + axes[i].get_position().x0) / 2
    fig.add_artist(plt.Line2D([x, x], [0.10, 0.90],
                              transform=fig.transFigure,
                              color='#B0B0B0', lw=0.8, ls='--'))

# Temperature gradient bar
arrow_ax = fig.add_axes([0.15, 0.02, 0.7, 0.055])
arrow_ax.set_xlim(0, 1)
arrow_ax.set_ylim(0, 1)
arrow_ax.set_xticks([])
arrow_ax.set_yticks([])
for spine in arrow_ax.spines.values():
    spine.set_visible(False)
arrow_ax.set_facecolor(BG_COLOR)

gradient = np.linspace(0, 1, 256).reshape(1, -1)
cmap = LinearSegmentedColormap.from_list('temp',
    ['#1B3A6B', '#4A90D9', '#D44A2B', '#E74C3C'])
arrow_ax.imshow(gradient, aspect='auto', cmap=cmap,
                extent=[0.05, 0.90, 0.2, 0.8])
arrow_ax.annotate('', xy=(0.94, 0.5), xytext=(0.90, 0.5),
                  arrowprops=dict(arrowstyle='-|>', color='#C0392B', lw=2))
arrow_ax.text(0.475, 0.5, 'Temperature  →', ha='center', va='center',
              fontsize=10, color='white', fontweight='bold',
              fontfamily='sans-serif')

plt.subplots_adjust(left=0.02, right=0.98, top=0.91, bottom=0.10, wspace=0.08)
plt.savefig('figures/3.phase-transition-v2.png', dpi=300, bbox_inches='tight',
            facecolor=BG_COLOR)
plt.close()
print("Saved to figures/3.phase-transition-v2.png")
