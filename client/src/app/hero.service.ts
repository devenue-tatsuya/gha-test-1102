// TODO: 動作確認できたら削除
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class HeroService {
  private url = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) {}

  getHeroes() {
    console.log('getHeroes');
    return this.http.get<any>(`${this.url}/api/heroes`);
  }
}
