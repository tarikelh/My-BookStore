import api from "../api";

interface Entity {
  id?: number;
}

export default abstract class BaseService<T extends Entity> {
  abstract get endpoint(): string;

  async getAll(): Promise<T[]> {
    const response = await api.get<T[]>(this.endpoint);
    console.log(`Fetching data from endpoint: ${this.endpoint}`);
    console.log(response.data, 'yoy');
    return response.data;
  }

  async getById(id: number): Promise<T> {
    const response = await api.get<T>(`${this.endpoint}/${id}/`);
    return response.data;
  }

  async save(entity: T): Promise<T> {
    const response = await api.post<T>(`${this.endpoint}/`, entity);
    return response.data;
  }

  async updateById(id: number, entity: Partial<T>): Promise<T> {
    const response = await api.put<T>(`${this.endpoint}/${id}`, entity);
    return response.data;
  }

  async deleteById(id: number): Promise<void> {
    await api.delete(`${this.endpoint}/${id}`);
  }
}
