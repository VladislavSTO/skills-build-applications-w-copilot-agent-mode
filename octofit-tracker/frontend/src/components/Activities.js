import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [users, setUsers] = useState([]);
  const [form, setForm] = useState({ user: '', activity_type: '', duration: '', distance: '' });
  const activityTypes = ['Бег', 'Велоспорт', 'Кроссфит', 'Силовая', 'Плавание'];
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetch('https://fluffy-space-meme-v5j4g4x4g9rfwvgj-8000.app.github.dev/api/activities/')
      .then(res => res.json())
      .then(data => setActivities(data));
    fetch('https://fluffy-space-meme-v5j4g4x4g9rfwvgj-8000.app.github.dev/api/users/')
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    fetch('https://fluffy-space-meme-v5j4g4x4g9rfwvgj-8000.app.github.dev/api/activities/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user: form.user,
        activity_type: form.activity_type,
        duration: Number(form.duration),
        distance: form.distance ? Number(form.distance) : null
      })
    })
      .then(async res => {
        if (!res.ok) {
          const err = await res.json();
          alert('Ошибка: ' + (err.detail || JSON.stringify(err)));
          setLoading(false);
          return null;
        }
        return res.json();
      })
      .then(newActivity => {
        if (newActivity) {
          setActivities([ ...activities, newActivity ]);
          setForm({ user: '', activity_type: '', duration: '', distance: '' });
        }
        setLoading(false);
      })
      .catch(() => setLoading(false));
  };

  return (
    <div className="container mt-4">
      <h1 className="mb-4 display-5">Activities</h1>
      <div className="card shadow mb-4">
        <div className="card-body">
          <form className="row g-3 mb-4" onSubmit={handleSubmit}>
            <div className="col-md-3">
              <select className="form-select" name="user" value={form.user} onChange={handleChange} required>
                <option value="">Select user...</option>
                {users.map(u => (
                  <option key={u._id} value={u._id}>{u.name} ({u.email})</option>
                ))}
              </select>
            </div>
            <div className="col-md-3">
              <select className="form-select" name="activity_type" value={form.activity_type} onChange={handleChange} required>
                <option value="">Тип активности...</option>
                {activityTypes.map(type => (
                  <option key={type} value={type}>{type}</option>
                ))}
              </select>
            </div>
            <div className="col-md-2">
              <input className="form-control" name="duration" type="number" min="1" placeholder="Duration (min)" value={form.duration} onChange={handleChange} required />
            </div>
            <div className="col-md-2">
              <input className="form-control" name="distance" type="number" step="0.01" placeholder="Distance (km)" value={form.distance} onChange={handleChange} />
            </div>
            <div className="col-md-2">
              <button className="btn btn-primary w-100" type="submit" disabled={loading}>{loading ? 'Adding...' : 'Add Activity'}</button>
            </div>
          </form>
          <table className="table table-striped table-hover">
            <thead className="table-primary">
              <tr>
                <th>Type</th>
                <th>Duration (min)</th>
                <th>Distance (km)</th>
                <th>User</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity, idx) => (
                <tr key={idx}>
                  <td>{activity.activity_type}</td>
                  <td>{activity.duration}</td>
                  <td>{activity.distance || '-'}</td>
                  <td>{users.find(u => u._id === activity.user)?.name || activity.user}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Activities;
