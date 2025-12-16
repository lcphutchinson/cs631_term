window.OrgDB = window.OrgDB || {};

OrgDB.loadEntityList = async function (config) {
  const container = document.getElementById(config.containerId);
  if (!container) return;

  const loadingEl = container.querySelector('.entity-loading');
  if (loadingEl) loadingEl.remove();

  const emptyLabel = container.dataset.emptyLabel || 'items';
  const emptyHint = container.dataset.emptyHint || '';

  try {
    const token = localStorage.getItem('access_token');
    const headers = token
      ? { 'Authorization': `Bearer ${token}` }
      : {};

    const response = await fetch(config.apiUrl, { headers });
    if (!response.ok) throw new Error('Failed to load data');

    const data = await response.json();
    console.log('Entity list response:', data);

    if (!Array.isArray(data)) {
      throw new Error('API did not return a list');
    }

    container.innerHTML = '';

    if (data.length === 0) {
      container.innerHTML = `
        <div class="py-10 text-center text-gray-500">
          <p class="text-lg font-medium">No ${emptyLabel} found</p>
          <p class="text-sm mt-1">${emptyHint}</p>
        </div>
      `;
      return;
    }

    data.forEach(entity => {
      container.insertAdjacentHTML(
        'beforeend',
        OrgDB.renderEntityCard(entity, config)
      );
    });

  } catch (err) {
    container.innerHTML = `
      <div class="py-10 text-center text-red-600">
        <p class="font-medium">Error loading ${emptyLabel}</p>
        <p class="text-sm mt-1">${err.message}</p>
      </div>
    `;
  }
};

OrgDB.renderEntityCard = function (entity, config) {
  return `
    <div
      class="bg-gray-50 border border-gray-200 rounded-lg p-4
             hover:bg-white hover:shadow transition"
    >
      <div class="flex justify-between items-start">
        <div>
          <h3 class="text-lg font-semibold text-gray-800">
            ${config.title(entity)}
          </h3>
          <p class="text-sm text-gray-600">
            ${config.subtitle ? config.subtitle(entity) : ''}
          </p>
        </div>

        <div class="flex space-x-3">
          <a href="${config.viewUrl(entity)}"
             class="text-blue-700 hover:text-blue-800 text-sm font-medium">
            View
          </a>
          ${config.editUrl ? `
            <a href="${config.editUrl(entity)}"
               class="text-gray-700 hover:text-gray-800 text-sm font-medium">
              Edit
            </a>
          ` : ''}
        </div>
      </div>
    </div>
  `;
};

OrgDB.openEditModal = function (config) {
  const root = document.getElementById('modalRoot');
  const form = document.getElementById('modalForm');

  document.getElementById('modalTitle').textContent = config.title;
  form.innerHTML = '';

  config.fields.forEach(f => {
    const value = config.initialData?.[f.name] ?? '';
    
    if (`${f.type}` == "radio"){
        form.insertAdjacentHTML('beforeend', `
          <div>
            <label class="text-m font-medium text-gray-700 ml-1 mr-4 mb-1">
              ${f.label}
            </label>
            <input
              required
              name=modalRadio
              type=radio
              value="${f.name}"
              ${value ? "checked" : ""}
              class="border rounded px-3 py-2"
            />
          `);
    }
    if (`${f.type}` == "checkbox") {
        form.insertAdjacentHTML('beforeend', `
          <div>
            <label class="text-m font-medium text-gray-700 ml-1 mr-4 mb-1">
              ${f.label}
            </label>
            <input
              name="${f.name}"
              type=checkbox
              ${value ? "checked" : ""}
              class="border rounded px-3 py-2"
            />
          </div>
        `);
    } else {
      form.insertAdjacentHTML('beforeend', `
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">
            ${f.label}
          </label>
          <input
            name="${f.name}"
            type="${f.type}"
            value="${value}"
            class="w-full border rounded px-3 py-2"
          />
        </div>
      `);
    }
    });

  root.classList.remove('hidden');

  form.onsubmit = async e => {
    e.preventDefault();

    const payload = {};
    new FormData(form).forEach((v, k) => {
      if (k == 'modalRadio') {
        const selectedRadio = document.querySelector('input[name="modalRadio"]:checked');
        payload[selectedRadio.value] = true
      }
      else if (v !== '') payload[k] = v;
    });
    
    console.log(payload)
    const res = await fetch(config.endpoint, {
      method: config.method || 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!res.ok) return alert('Save failed');

    const updated = payload;
    config.onSuccess?.(updated);
    OrgDB.closeModal();
  };

  document.getElementById('modalCancel').onclick = OrgDB.closeModal;
};

OrgDB.closeModal = function () {
  document.getElementById('modalRoot').classList.add('hidden');
};


